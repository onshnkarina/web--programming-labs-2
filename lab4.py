from flask import Blueprint, render_template, request, redirect, session
lab4 = Blueprint('lab4', __name__)
 
@lab4.route('/lab4/')
def lab():
    return render_template('lab4/lab4.html')

@lab4.route('/lab4/div-form')
def div_form():
    return render_template('lab4/div-form.html')

@lab4.route('/lab4/sum-form')
def sum_form():
    return render_template('lab4/sum-form.html')
@lab4.route('/lab4/umn-form')
def mul_form():
    return render_template('lab4/umn-form.html')
@lab4.route('/lab4/sub-form')
def sub_form():
    return render_template('lab4/sub-form.html')
@lab4.route('/lab4/st-form')
def pow_form():
    return render_template('lab4/st-form.html')

@lab4.route('/lab4/div', methods=['POST'])
def div():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if  x1 =='' or  x2 == '':
        return render_template('lab4/div.html', error='Оба поля должны быть заполнены!')
    
    x1 = float(x1)
    x2 = float(x2)
    if x2 == 0:
        return render_template('lab4/div.html', error='На ноль делить нельзя!')
    result = x1 / x2
    return render_template('lab4/div.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/sum', methods=['POST'])
def sum():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    x1 = float(x1) if x1 else 0
    x2 = float(x2) if x2 else 0
    result = x1 + x2
    return render_template('lab4/sum.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/umn', methods=['POST'])
def umn():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    x1 = float(x1) if x1 else 1
    x2 = float(x2) if x2 else 1
    result = x1 * x2
    return render_template('lab4/umn.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/sub', methods=['POST'])
def sub():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 =='' or x2 == '':
        return render_template('lab4/sub.html', error='Оба поля должны быть заполнены!')
    x1 = float(x1)
    x2 = float(x2)
    result = x1 - x2
    return render_template('lab4/sub.html', x1=x1, x2=x2, result=result)

@lab4.route('/lab4/st', methods=['POST'])
def st():
    x1 = request.form.get('x1')
    x2 = request.form.get('x2')
    if x1 == '' or x2 == '':
        return render_template('lab4/st.html', error='Оба поля должны быть заполнены!')
    x1 = float(x1)
    x2 = float(x2)
    if x1 == 0 and x2 == 0:
        return render_template('lab4/st.html', error='0 в степени 0 не определено!')
    result = x1 ** x2
    return render_template('lab4/st.html', x1=x1, x2=x2, result=result)

tree_count = 0
@lab4.route('/lab4/tree', methods = ['GET', 'POST'])
def tree():
    global tree_count
    if request.method == 'GET':
        return render_template('lab4/tree.html', tree_count=tree_count)
    
    operation = request.form.get('operation')
    if operation == 'cut':
        tree_count -= 1
    elif operation == 'plant':
        tree_count +=1
    
    return redirect ('/lab4/tree')

users = [
    {'login': 'alex', 'password': '123', 'name': 'Alex Helson', 'gender': 'male'},
    {'login': 'bob', 'password': '555', 'name': 'Bob Uinston', 'gender': 'male'},
    {'login': 'max', 'password': '666', 'name': 'Max Richards', 'gender': 'male'},
    {'login': 'sam', 'password': '5858', 'name': 'Sam Brown', 'gender': 'male'},
]

@lab4.route('/lab4/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if 'login' in session:
            authorized = True
            login = session['login']
            name = next(user['name'] for user in users if user['login'] == login)
        else:
            authorized = False
            login = ''
            name = ''
        return render_template('lab4/login.html', authorized=authorized, login=login, name=name)
    
    login = request.form.get('login')
    password = request.form.get('password')

    if not login:
        error = 'Не введён логин'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)
    if not password:
        error = 'Не введён пароль'
        return render_template('lab4/login.html', error=error, authorized=False, login=login)

    for user in users:
        if login == user['login'] and password == user['password']:
            session['login'] = login  
            return redirect('/lab4/login') 
    
    error = 'Неверные логин и/или пароль'
    return render_template('lab4/login.html', error=error, authorized=False, login=login)

@lab4.route('/lab4/logout', methods=['POST'])
def logout():
    session.pop('login', None)
    return redirect('/lab4/login')

@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    if request.method == 'GET':
        return render_template('lab4/fridge.html')
    temperature = request.form.get('temperature')
    if not temperature:
        error = 'Ошибка: не задана температура'
        return render_template('lab4/fridge.html', error=error)
    try:
        temp = float(temperature)
    except ValueError:
        error = 'Ошибка: температура должна быть числом'
        return render_template('lab4/fridge.html', error=error)
    snowflakes = None
    if temp < -12:
        message = 'Не удалось установить температуру — слишком низкое значение'
    elif temp > -1:
        message = 'Не удалось установить температуру — слишком высокое значение'
    elif -12 <= temp <= -9:
        message = f'Установлена температура: {temp}°С'
        snowflakes = 3 
    elif -8 <= temp <= -5:
        message = f'Установлена температура: {temp}°С'
        snowflakes = 2 
    elif -4 <= temp <= -1:
        message = f'Установлена температура: {temp}°С'
        snowflakes = 1
    else:
        message = 'Неизвестная ошибка'
    return render_template('lab4/fridge.html', message=message, snowflakes=snowflakes)

corn = {
    'barley': {'name': 'ячмень', 'price': 12345},
    'oats': {'name': 'овёс', 'price': 8522},
    'wheat': {'name': 'пшеница', 'price': 8722},
    'rye': {'name': 'рожь', 'price': 14111}
}
@lab4.route('/lab4/zerno', methods=['GET', 'POST'])
def zerno():
    if request.method == 'POST':
        grain = request.form.get('grain')
        weight = request.form.get('weight')
        if not weight:
            message = "Ошибка: укажите вес заказа."
            return render_template('lab4/zerno.html', message=message)
        try:
            weight = float(weight)
        except ValueError:
            message = "Ошибка: веведите число."
            return render_template('lab4/zerno.html', message=message)
        if weight <= 0:
            message = "Ошибка: вес должен быть больше 0."
            return render_template('lab4/zerno.html', message=message)
        if weight > 500:
            message = "Такого объёма сейчас нет в наличии."
            return render_template('lab4/zerno.html', message=message)
        grain_info = corn.get(grain)
        price_ton = grain_info['price']
        grain_name_ru = grain_info['name']
        total_price = weight * price_ton
        discount_message = None
        if weight > 50:
            discount = 0.1  
            sk = total_price / 10
            total_price *= (1 - discount)
            discount_message = f"Применена скидка 10% за большой объём. Размер скидки: {sk} руб"
        message = f"Заказ успешно сформирован. Вы заказали {grain_name_ru}. Вес: {weight} т. Сумма к оплате: {total_price:.2f} руб."
        return render_template('lab4/zerno.html', message=message, discount=discount_message)
    return render_template('lab4/zerno.html')


@lab4.route('/lab4/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        name = request.form.get('name')
        if not login or not password or not name:
            error = 'Заполните все поля.'
            return render_template('lab4/reg.html', error=error)
        
        if any(user['login'] == login for user in users):
            error = 'Логин уже занят.'
            return render_template('lab4/reg.html', error=error)
        
        users.append({'login': login, 'password': password, 'name': name, 'gender': 'unknown'})
        return redirect('/lab4/login')
    
    return render_template('lab4/reg.html')

@lab4.route('/lab4/users')
def users_spisok():
    if 'login' not in session:
        return redirect('/lab4/login')
    
    current_user = next(user for user in users if user['login'] == session['login'])
    return render_template('lab4/users.html', users=users, current_user=current_user)

@lab4.route('/lab4/delete', methods=['POST'])
def delete_user():
    login = request.form.get('login')
    users[:] = [user for user in users if user['login'] != login]
    session.pop('login', None)
    return redirect('/lab4/login')


@lab4.route('/lab4/redact', methods=['GET', 'POST'])
def redact_user():
    if 'login' not in session:
        return redirect('/lab4/login')
    
    current_user = next(user for user in users if user['login'] == session['login'])
    
    if request.method == 'POST':
        new_name = request.form.get('name')
        new_password = request.form.get('password')
        
        if new_name:
            current_user['name'] = new_name
        if new_password:
            current_user['password'] = new_password
        
        return redirect('/lab4/users')
    
    return render_template('lab4/redact.html', user=current_user)