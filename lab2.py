from flask import Blueprint, url_for, redirect, render_template, request
lab2 = Blueprint('lab2',__name__)

@lab2.route('/lab2/a')
def a():
    return 'без слэша'


@lab2.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']


@lab2.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "такого цветка нет", 404
    del flower_data[flower_id]
    return redirect(url_for('show_all_flowers'))


@lab2.route('/lab2/add_flowers', methods=['POST']) 
def add_flowers():  
    name = request.form.get('name')  
    price = request.form.get('price') 
    if not name or not price:  
        return "Неверные данные", 400  
    flower_data.lab2end({'name': name, 'price': int(price)})  
                                                            
    return redirect(url_for('show_all_flowers')) 


@lab2.route('/lab2/flowers')
def show_all_flowers():
   return render_template('lab2/flowers.html', flowers=flower_data)


@lab2.route('/lab2/clearflowers')
def clear_flowers():
    flower_list.clear()  
    return redirect(url_for('show_all_flowers'))


@lab2.route('/lab2/delete_flower/<int:flower_id>')
def delete_flower(flower_id):
    if flower_id >= len(flower_data):
        return "Такого цветка нет", 404
    del flower_data[flower_id]
    return redirect(url_for('show_all_flowers'))


@lab2.route('/lab2/example')
def example():
    name = 'Онищенко Арина'
    laba = '2'
    group = 'ФБИ-24'
    course ='3'
    fruits = [
        {'name': 'яблоки', 'price': 100}, 
        {'name': 'груши', 'price': 120}, 
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95}, 
        {'name': 'манго', 'price': 321}
    ]
    return render_template('lab2/example.html', name=name, course=course, laba=laba, 
                           group=group, fruits=fruits)


@lab2.route('/lab2/')
def lab():
    return render_template('lab2/lab2.html')


@lab2.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('lab2/filter.html', phrase = phrase)


@lab2.route('/lab2/calc/<int:a>/<int:b>')
def calc(a, b):
    sum_result = a + b
    sub_result = a - b
    mul_result = a * b
    div_result = "Деление на ноль невозможно" if b == 0 else a / b
    pow_result = a ** b
    return f'''
<!doctype html>
<html>
    <body>
    <h1> Расчет с параметрами </h1>
    <p>{a} + {b} = {sum_result}</p>
    <p>{a} - {b} = {sub_result}</p>
    <p>{a} * {b} = {mul_result}</p>
    <p>{a} / {b} = {div_result}</p>
    <p>{a} <sup> {b} </sup>= {pow_result}</p>
    </body>
</html>
'''


@lab2.route('/lab2/calc/')
def redirect_to_default():
    return redirect('/lab2/calc/1/1')


@lab2.route('/lab2/calc/<int:a>')
def redirect_with_default_b(a):
    return redirect(f'/lab2/calc/{a}/1')

book_spisok = [
    {"author": "Михаил Булгаков", "title": "Мастер и Маргарита", "genre": "Роман", "pages": 504},
    {"author": "Габриэль Гарсия Маркес", "title": "Сто лет одиночества", "genre": "Роман", "pages": 422},
    {"author": "Джордж Оруэлл", "title": "1984", "genre": "Антиутопия", "pages": 328},
    {"author": "Фёдор Достоевский", "title": "Преступление и наказание", "genre": "Роман", "pages": 430},
    {"author": "Лев Толстой", "title": "Анна Каренина", "genre": "Роман", "pages": 864},
    {"author": "Стивен Кинг", "title": "Сияние", "genre": "Ужасы", "pages": 447},
    {"author": "Джордж Мартин", "title": "Игра престолов", "genre": "Фэнтези", "pages": 694},
    {"author": "Сент-Экзюпери Антуан де", "title": "Маленький принц", "genre": "Сказка", "pages": 96},
    {"author": "Льюис Кэрролл", "title": "Алиса в стране чудес", "genre": "Сказка", "pages": 96},
    {"author": "Джейн Остин", "title": "Гордость и предубеждение", "genre": "Роман", "pages": 432}
]


@lab2.route('/lab2/books')
def show_books():
    return render_template('lab2/books.html', books=book_spisok)

dogs = [
    {"name": "Кавалер-кинг-чарльз-спаниель", "description": "Эта порода была названа в честь короля Карла II, который жил в 17 веке. Он не имел прямого отношения к разведению собак, но во время его правления для маленьких спаниелей все двери были открыты.", 
    "image": "kav.jpg"},
    {"name": "Мальтипу", "description": "Мальтипу – наполовину той-пудель, наполовину мальтийская болонка. Порода расценивается как дизайнерская, но остается не признанной международными кинологическими ассоциациями. © «Lapkins.ru» Копирование материалов запрещено.В целом метисы болонки и пуделя – неконфликтные и уживчивые питомцы, охотно делящие жилплощадь с другими домашними животными.  © «Lapkins.ru» Копирование материалов запрещено.",
     "image": "mal.jpg"},
    {"name": "Шпиц", "description": "Дальние родственники шпицев — эскимосские собаки и самоедские лайки. Представители этой породы приобрели свои миниатюрные размеры лишь благодаря селекции.Независимо от размера, шпиц ощущает себя большой собакой, поэтому часто имеет задиристый характер.",
     "image": "shp.jpg"},
    {"name": "Мальтезе. Мальтийская болонка", "description": "Предположительно, родственниками мальтезе являются пудели и спаниели. Свое название порода получила в 16-ом в., когда ее представители в большом количестве обитали на острове Мальта, однако сюда белые болонки были завезены за несколько столетий, с побережья Адриатического моря.",
     "image": "malt.jpg"},
    {"name": "Лабрадор-ретривер", "description": "Лабрадор-ретривер – одна из самых популярных в мире пород. Про лабрадоров снимают фильмы, их фотографиями пестрят социальные сети. Такая популярность лабрадоров не зависит от моды и вполне заслужена. Это одна из лучших собак-компаньонов среди всего многообразия пород.",
     "image": "labr.jpg"},
    {"name": "Бигль", "description": "Бигль относится к породам собак среднего размера, выведенных для охоты. Согласно классификации FCI порода принадлежит группе гончих маленького размера. Собака этой породы хорошо подходит для содержания в квартире, очень общительна и дружелюбна. Бигль любит бегать и всегда энергичен, поэтому может стать отличным спутником для прогулок на свежем воздухе вместе с хозяином.",
     "image": "bgl.jpg"}
]


@lab2.route('/lab2/dogs')
def show_dogs():
    return render_template('lab2/dogs.html', dogs=dogs)

flower_data = [
    {'name': 'роза', 'price': 150},
    {'name': 'тюльпан', 'price': 100},
    {'name': 'незабудка', 'price': 50},
    {'name': 'ромашка', 'price': 75},
]

