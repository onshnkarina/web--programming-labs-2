from flask import Flask, redirect, url_for
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4
from lab5 import lab5
from lab6 import lab6
from lab7 import lab7
from lab8 import lab8
from lab9 import lab9
from rgz_5 import rgz_5
import os
from os import path
from flask_sqlalchemy import SQLAlchemy
from db import db
from db.models import users
from flask_login import LoginManager

app = Flask(__name__)

login_manager = LoginManager()
login_manager.login_view = 'lab8.login'
login_manager.init_app(app)
@login_manager.user_loader
def load_users(login_id):
    return users.query.get(int(login_id))

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'секретно-секретный секрет')
app.config['DB_TYPE'] = os.getenv('DB_TYPE', 'postgres')
app.config['UPLOAD_FOLDER'] = path.join('static', 'uploads')
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

if app.config['DB_TYPE'] == 'postgres':
    db_name = 'ar_onishenko'
    db_user = 'ar_onishenko'
    db_password = '123'
    host_ip = '127.0.0.1'
    host_port = 5432
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        f'postgresql://{db_user}:{db_password}@{host_ip}:{host_port}/{db_name}'
else:
    dir_path = path.dirname(path.realpath(__file__))
    db_path = path.join(dir_path, "ar_onishenko.db")
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
    
db.init_app(app)


app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)
app.register_blueprint(lab5)
app.register_blueprint(lab6)
app.register_blueprint(lab7)
app.register_blueprint(lab8)
app.register_blueprint(lab9)
app.register_blueprint(rgz_5)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu ():
    return """
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1/lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header»
        <main>
            <nav>
            <ul>
                <li><a href="/lab1">Первая лабораторная</a></li>
                <li><a href="/lab2">Вторая лабораторная</a></li>
                <li><a href="/lab3">Третья лабораторная</a></li>
                <li><a href="/lab4">Четвертая лабораторная</a></li>
                <li><a href="/lab5">Пятая лабораторная</a></li> 
                <li><a href="/lab6">Шестая лабораторная</a></li>  
                <li><a href="/lab7">Седьмая лабораторная</a></li>  
                <li><a href="/lab8">Восьмая лабораторная</a></li>  
                <li><a href="/lab9">Девятая лабораторная</a></li> 
                <li><a href="/rgz">РГЗ</a></li>
            </ul>
        </nav>
        </main>

        <footer>
            &copy; Онищенко Арина, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""

    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1/autumn.css') + '''">
    </head>
    <body>
        <h1>Интересные факты об осени</h1>
    
        <p >До 18 века на Руси считалось, что осень начинается не 1, а 23 сентября, а заканчивалась 25 декабря.</p>

        <p>В Южном полушарии осенними месяцами являются март, апрель и май. </p>

        <p>Осенняя депрессия — реально существующий диагноз. Ей подвержено около 5 % населения стран, в которых осень есть.</p>
        <p>Мокрые листья, усеивающие дорогу каждую осень, очень скользки. На них может легко упасть пешеход, а тормозной путь автомобиля на 
        листьях удлиняется в 5–10 раз.</p>
        <img style="border-radius: 10px;" src="''' + url_for('static',filename='lab1/autumn.jpg') + '''">
    </body>
</html>
'''