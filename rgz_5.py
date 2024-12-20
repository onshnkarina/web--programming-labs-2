from flask import Blueprint,  render_template, request, redirect, jsonify, session, current_app
from os import path
import sqlite3
import psycopg2
from psycopg2.extras import RealDictCursor
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
import os
rgz_5 = Blueprint('rgz_5', __name__)


def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host='127.0.0.1',
            database='arina_onishchenko_knowledge_base',
            user='arina_onishchenko_knowledge_base',
            password='123',
            options="-c client_encoding=UTF8"
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()

    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()


@rgz_5.route('/rgz')
def rgz():
    return render_template('rgz/login.html')


@rgz_5.route('/rgz/rest-api/users/registration', methods=['POST'])
def add_user():
    data = request.get_json()
  
    if not data.get('username'):
        return {'username': 'Придумайте свой ник'}, 400
    if not data.get('password'):
        return {'password': 'Заполните пароль'}, 400
    
    password_hash = generate_password_hash(data['password'])
    try:
        conn, cur = db_connect()

        if current_app.config['DB_TYPE'] == 'postgres':

            cur.execute(
                "INSERT INTO users (username, password) VALUES (%s, %s) RETURNING id",
                (data['username'], password_hash)
            )
            new_user_id = cur.fetchone()['id']
        else:
    
            cur.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (data['username'], password_hash)
            )
            new_user_id = cur.fetchone()  
        
        db_close(conn, cur)
        return {"index": new_user_id}, 201

    except Exception as e:
        db_close(conn, cur)
        return {'exception': str(e)}, 400


@rgz_5.route('/rgz/rest-api/users/login', methods=['POST'])
def login_user():
    data = request.get_json()

    # Проверка обязательных полей
    if not data.get('username'):
        return {'username': 'Введите никнэйм'}, 400
    if not data.get('password'):
        return {'password': 'Введите пароль'}, 400

    conn = None  # Инициализация переменной conn
    cur = None  # Инициализация переменной cur

    try:
        conn, cur = db_connect()  # Подключение к базе данных

        # Выполнение запроса для поиска пользователя
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("SELECT id, username, password FROM users WHERE username = %s", (data['username'],))
        else:
            cur.execute("SELECT id, username, password FROM users WHERE username = ?", (data['username'],))

        user = cur.fetchone()  # Получение результата запроса

        # Проверка, найден ли пользователь
        if not user:
            return {'username': 'Пользователь не найден'}, 400

        # Извлечение данных пользователя
        user_id = user['id']
        username = user['username']
        password_hash = user['password']

        # Проверка пароля
        if not check_password_hash(password_hash, data['password']):
            return {'password': 'Неверный пароль'}, 400

        # Установка сессии
        session['user_id'] = user_id
        session['username'] = username

        return {}, 200  # Успешный вход

    except Exception as e:
        # Обработка исключений
        return {'exception': str(e)}, 400

    finally:
        # Закрытие соединения с базой данных
        if conn and cur:
            db_close(conn, cur)
@rgz_5.route('/main')
def rgz_5_main_page():
    if 'user_id' not in session:
        return redirect('/rgz')  
    
    try:
        user_id = session['user_id']
        conn, cur = db_connect()

        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("SELECT * FROM profiles WHERE user_id = %s", (user_id,))
        else:
            cur.execute("SELECT * FROM profiles WHERE user_id = ?", (user_id,))
        
        profile = cur.fetchone()

        profile_filled = bool(profile)

        db_close(conn, cur)

        # Проверяем, найден ли профиль
        if profile:
            photo_path = profile['photo_path'] if current_app.config['DB_TYPE'] == 'postgres' else profile['photo_path']
            profile = dict(profile)  
            if photo_path:
                profile['photo_path'] = str(photo_path).replace('\\', '/')

            gender_map = {
                "male": "мужской",
                "female": "женский"
            }
            profile['gender'] = gender_map.get(profile['gender'], profile['gender'])
            looking_for_map = {
                "male": "мужской",
                "female": "женский"
            }
            profile['looking_for'] = looking_for_map.get(profile['looking_for'], profile['looking_for'])
        else:
            return render_template('rgz/main.html')  

        return render_template('rgz/main.html', username=session['username'], profile=profile, profile_filled= profile_filled)
    
    except Exception as e:
        return {'message': str(e)}, 500

@rgz_5.route('/rgz/rest-api/profiles', methods=['POST'])
def add_profile():
    user_id = session['user_id'] 

    if 'user_id' not in session:
        current_app.logger.warning("Пользователь не авторизован.")
        return {'message': 'Не авторизован'}, 403


    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    looking_for = request.form.get('looking_for')
    about = request.form.get('about', '')
    photo = request.files.get('photo')

    if not name or not age or not gender or not looking_for:
        return {'message': 'Заполните все обязательные поля'}, 400

    photo_path = None
    if photo:
        filename = secure_filename(f"user_{user_id}_{photo.filename}")
        upload_folder = current_app.config['UPLOAD_FOLDER']
        if current_app.config['DB_TYPE'] != 'postgres':
            upload_folder = 'web-programming-labs/' + upload_folder

        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder) 
        
        save_path = os.path.join(upload_folder, filename)
        photo.save(save_path)
        photo_path = os.path.join('uploads', filename)

    try:
        conn, cur = db_connect()
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(
                """
                INSERT INTO profiles (user_id, name, age, gender, looking_for, about, photo_path)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """,
                (user_id, name, age, gender, looking_for, about, photo_path),
            )
        else:
            cur.execute(
                """
                INSERT INTO profiles (user_id, name, age, gender, looking_for, about, photo_path)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (user_id, name, age, gender, looking_for, about, photo_path),
            )
        conn.commit()
        db_close(conn, cur)

        return {'message': 'Профиль успешно добавлен'}, 201

    except Exception as e:
        current_app.logger.error(f"Ошибка при добавлении профиля: {str(e)}")
        db_close(conn, cur)
        return {'message': str(e)}, 500

    
@rgz_5.route('/rgz/rest-api/profiles', methods=['PUT'])
def update_profile():
    if 'user_id' not in session:
        return {'message': 'Не авторизован'}, 403

    user_id = session['user_id']
    name = request.form.get('name')
    age = request.form.get('age')
    gender = request.form.get('gender')
    looking_for = request.form.get('looking_for')
    about = request.form.get('about', '')
    photo = request.files.get('photo')
    is_hidden = request.form.get('is_hidden') == 'true'

    if not name or not age or not gender or not looking_for:
        return {'message': 'Заполните все обязательные поля'}, 400

    photo_path = None
    if photo:
        filename = secure_filename(f"user_{user_id}_{photo.filename}")
        upload_folder = current_app.config['UPLOAD_FOLDER']
        if current_app.config['DB_TYPE'] != 'postgres':
            upload_folder = 'web-programming-labs/' + upload_folder

        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder) 
        
        save_path = os.path.join(upload_folder, filename)
        photo.save(save_path)
        photo_path = os.path.join('uploads', filename)

    try:
        conn, cur = db_connect()
        
       
        if photo_path:
            query_postgres = """
                UPDATE profiles
                SET name = %s, age = %s, gender = %s, looking_for = %s, about = %s, photo_path = %s, is_hidden = %s
                WHERE user_id = %s
            """
            query_sqlite = """
                UPDATE profiles
                SET name = ?, age = ?, gender = ?, looking_for = ?, about = ?, photo_path = ?, is_hidden = ?
                WHERE user_id = ?
            """
            params = (name, age, gender, looking_for, about, photo_path, is_hidden, user_id)
        else:
            query_postgres = """
                UPDATE profiles
                SET name = %s, age = %s, gender = %s, looking_for = %s, about = %s, is_hidden = %s
                WHERE user_id = %s
            """
            query_sqlite = """
                UPDATE profiles
                SET name = ?, age = ?, gender = ?, looking_for = ?, about = ?, is_hidden = ?
                WHERE user_id = ?
            """
            params = (name, age, gender, looking_for, about, is_hidden, user_id)

        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute(query_postgres, params)
        else:
            cur.execute(query_sqlite, params)

        conn.commit()
        db_close(conn, cur)
        return {'message': 'Профиль успешно обновлен'}, 200
    except Exception as e:
        return {'message': str(e)}, 500

@rgz_5.route('/rgz/rest-api/profiles/delete', methods=['DELETE'])
def delete_profile():
    if 'user_id' not in session:
        return {'message': 'Не авторизован'}, 403

    user_id = session['user_id']

    try:
        conn, cur = db_connect()
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("DELETE FROM profiles WHERE user_id = %s", (user_id,))
        else:
            cur.execute("DELETE FROM profiles WHERE user_id = ?", (user_id,))
        db_close(conn, cur)
        conn.commit()
        session.clear()
        return {'message': 'Аккаунт успешно удален'}, 200
    except Exception as e:
        return {'message': str(e)}, 500



@rgz_5.route('/rgz/rest-api/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect('/rgz')


@rgz_5.route('/rgz/rest-api/search', methods=['GET'])
def search_profiles():
    if 'user_id' not in session:
        return {'message': 'Не авторизован'}, 403

    search_name = request.args.get('name', '').strip()
    search_age = request.args.get('age')
    offset = int(request.args.get('offset', 0)) 
    limit = 3  

    user_id = session['user_id']
    try:
        conn, cur = db_connect()

        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("""
                SELECT gender, looking_for FROM profiles WHERE user_id = %s
            """, (user_id,))
        else:
            cur.execute("""
                SELECT gender, looking_for FROM profiles WHERE user_id = ?
            """, (user_id,))
        
        user_profile = cur.fetchone()
        if not user_profile:
            db_close(conn, cur)
            return {'message': 'Профиль не найден'}, 404
        
        user_gender = user_profile['gender']
        user_looking_for = user_profile['looking_for']

        if current_app.config['DB_TYPE'] == 'postgres':
            query = """
                SELECT name, age, gender, about, photo_path
                FROM profiles
                WHERE is_hidden = FALSE
                AND gender = %s
                AND looking_for = %s
            """
            params = [user_looking_for, user_gender]

            if search_name:
                query += " AND name ILIKE %s"
                params.append(f"%{search_name}%")

            if search_age:
                query += " AND age = %s"
                params.append(search_age)

            query += " LIMIT %s OFFSET %s"
            params.extend([limit, offset])

        else:
            query = """
                SELECT name, age, gender, about, photo_path
                FROM profiles
                WHERE is_hidden = 0
                AND gender = ?
                AND looking_for = ?
            """
            params = [user_looking_for, user_gender]

            if search_name:
                query += " AND name LIKE ?"
                params.append(f"%{search_name}%")

            if search_age:
                query += " AND age = ?"
                params.append(search_age)

            query += " LIMIT ? OFFSET ?"
            params.extend([limit, offset])

        cur.execute(query, tuple(params))
        results = cur.fetchall()
        db_close(conn, cur)

        

        return jsonify([dict(row) for row in results]), 200

    except Exception as e:
        return {'message': str(e)}, 500