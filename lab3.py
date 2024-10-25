from flask import Blueprint, render_template, request, make_response, redirect
lab3 = Blueprint('lab3',__name__)

@lab3.route('/lab3/')
def lab():
    name = request.cookies.get('name', "Неизвестный")
    age = request.cookies.get('age', "Неизвестен")
    name_color = request.cookies.get('name_color')
    return render_template('lab3/lab3.html', name=name, name_color=name_color, age=age)


@lab3.route('/lab3/cookie')
def cookie():
    resp = make_response(redirect('/lab3/'))
    resp.set_cookie('name', 'Alex', max_age=5)
    resp.set_cookie('age', '20')
    resp.set_cookie('name_color', 'magenta')
    return resp


@lab3.route('/lab3/del_cookie')
def del_cookie():
    resp = make_response(redirect('/lab3/'))
    resp.delete_cookie('name')
    resp.delete_cookie('age')
    resp.delete_cookie('name_color')
    return resp


@lab3.route('/lab3/form1')
def form1():
    errors={}
    user = request.args.get('user')
    if user == '':
        errors['user']= 'Заполните поле!'
    
    age = request.args.get('age') 
    if age == '':
        errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex')
    return render_template('lab3/form1.html', user=user, age=age, sex=sex, errors=errors)



@lab3.route('/lab3/order')
def order():

    return render_template('lab3/order.html')


@lab3.route('/lab3/pay')
def pay():
        price=0
        drink = request.args.get('drink')
        #Пусть кофе стоит 120 рублей, черный чай - 80 рублей, зеленый - 70 рублей.
        if drink == 'coffee':
             price= 120
        elif drink == 'black-tea':
             price = 80
        else:
             price=70
        #Добавка молодка удорожает напиток на 30 рублей, а сахар - на 10.
        if request.args.get('milk') == 'on':
             price += 30
        if request.args.get('sugar') == 'on':
             price += 10
        return render_template('lab3/pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    price = request.args.get('price')
    return render_template('lab3/success.html', price=price)


@lab3.route('/lab3/settings')
def settings():
    color = request.args.get('color')
    f_color = request.args.get('f_color')
    font_size = request.args.get('font_size')
    font_style = request.args.get('font_style')
    if color or f_color or font_size:
        resp = make_response (redirect ('/lab3/settings'))
        if color:
            resp.set_cookie('color', color)
        if f_color:
            resp.set_cookie('f_color', f_color)
        if font_size:
           resp.set_cookie('font_size', font_size) 
        if font_style:
            resp.set_cookie('font_style', font_style) 
        return resp
    color = request.cookies.get ( 'color')
    f_color = request.cookies.get('f_color')
    font_size = request.cookies.get('font_size', '16')
    font_style = request.cookies.get('font_style')
    resp = make_response(render_template ('lab3/settings.html', color=color, f_color=f_color, 
                                             font_size=font_size, font_style=font_style))
    return resp


@lab3.route('/lab3/ticket')
def ticket():
    passenger_name = request.args.get('passenger_name')
    polka_type = request.args.get('polka_type')
    with_bedding = request.args.get('with_bedding')
    with_luggage = request.args.get('with_luggage')
    age = request.args.get('age')
    departure_point = request.args.get('departure_point')
    destination_point = request.args.get('destination_point')
    travel_date = request.args.get('travel_date')
    strahovka = request.args.get('strahovka')
    if passenger_name and polka_type and age and departure_point and destination_point and travel_date:
        age = int(age)
        
        ticket_price = 1000 if age >= 18 else 700  
        if polka_type in ['lower', 'lower_side']:
            ticket_price += 100
        if with_bedding == 'on':
            ticket_price += 75
        if with_luggage == 'on':
            ticket_price += 250
        if strahovka == 'on':
            ticket_price += 150
        ticket_type = "Детский билет" if age < 18 else "Взрослый билет"
        return render_template('lab3/tick_chek.html', 
                               passenger_name=passenger_name, 
                               ticket_type=ticket_type,
                               ticket_price=ticket_price,
                               departure_point=departure_point,
                               destination_point=destination_point,
                               travel_date=travel_date)
    return render_template('lab3/ticket.html')


@lab3.route('/lab3/clear_cookies')
def clear_cookies():
    resp = make_response(redirect('/lab3/settings'))
    
    
    resp.delete_cookie('color')
    resp.delete_cookie('f_color')
    resp.delete_cookie('font_size')
    resp.delete_cookie('font_style')
    
    return resp