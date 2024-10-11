from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

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
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <header>
            НГТУ, ФБ, WEB-программирование, часть 2. Список лабораторных
        </header»
        <main>
            <h2 style="margin-left: 1.3%;">Меню</h2>
            <a href='http://127.0.0.1:5000/lab1'>Лабораторная работа 1</a>
        </main>

        <footer>
            &copy; Онищенко Арина, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""
@app.route("/lab1")
def lab1():
    return """
<!doctype html>
<html>
    <head>
        <title›Онищенко Арина Сергеевна, лабораторная 1</title>
    </head>
    <body>
        <header>
            НГТУ, ОБ, Лабораторная работа 1
        </header»

        <h1>web-сервер на flasks</h1>
        <p>
            Flask — фреймворк для создания веб-приложений на языке
            программирования Python, использующий набор инструментов
            Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
            называемых микрофреймворков — минималистичных каркасов
            веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </p>
        <a href="/menu">Меню</a>
        <h2>Реализованные роуты</h2>
        <div>
            <ol>
                <li>
                    <a href="lab1/oak">Дуб</a>
                </li>
                <li>
                    <a href="lab1/student">Студент</a>
                </li>
                <li>
                    <a href="lab1/python">Python</a>
                </li>
                <li>
                    <a href="lab1/autumn">Осень</a>
                </li>
            
            </ol>
        </div>

        <footer>
            &copy; Онищенко Арина, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""
@app.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
        <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
    </head>
    <body>
        <h1>Дуб</h1>
        <img src="''' + url_for('static',filename='oak.jpg') + '''">
    </body>
</html>
'''
@app.route('/lab1/student')
def student():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='student.css') + '''">
    </head>
    <body>
        <h1>Онищенко Арина Сергеевна</h1>
        <img src="''' + url_for('static',filename='logo.png') + '''">
    </body>
</html>
'''
@app.route('/lab1/python')
def python():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='python.css') + '''">
    </head>
    <body>
        <h1>Интересные факты о языке Python</h1>
    
        <p >В декабре 1989 года создатель Python Гвидо Ван Россум думал над хобби-проектом, 
        чтобы занять себя в последнюю неделю перед Рождеством. Он думал о написании нового языка 
        сценариев, который будет потомком ABC и хотел написать его на C. Он решил назвать его Python.</p>

        <p>Название языка не имеет ничего общего со змеями, он назван так в честь популярной британской 
        комедийной труппы Монти Пайтона из 1970ых. Гвидо является большим фанатом «Летающего Цирка Монти Пайтона». 
        Находясь в довольно мрачном настроении, он и назвал проект «Python». </p>

        <p>Согласно недавнему опросу, в 2015 году в Великобритании Python обогнал французский и стал самым популярным 
        языком в начальных школах. Из 10 родителей, 6 предпочли, чтобы их дети изучали Python, а не французский.</p>
        <img style="border-radius: 10px;" src="''' + url_for('static',filename='python.jpg') + '''">
    </body>
</html>
'''
@app.route('/lab1/autumn')
def autumn():
    return '''
<!DOCTYPE html>
<html lang="ru">
    <head>
        <link rel="stylesheet" href="''' + url_for('static', filename='autumn.css') + '''">
    </head>
    <body>
        <h1>Интересные факты об осени</h1>
    
        <p >До 18 века на Руси считалось, что осень начинается не 1, а 23 сентября, а заканчивалась 25 декабря.</p>

        <p>В Южном полушарии осенними месяцами являются март, апрель и май. </p>

        <p>Осенняя депрессия — реально существующий диагноз. Ей подвержено около 5 % населения стран, в которых осень есть.</p>
        <p>Мокрые листья, усеивающие дорогу каждую осень, очень скользки. На них может легко упасть пешеход, а тормозной путь автомобиля на 
        листьях удлиняется в 5–10 раз.</p>
        <img style="border-radius: 10px;" src="''' + url_for('static',filename='autumn.jpg') + '''">
    </body>
</html>
'''
@app.route('/lab2/a')
def a():
    return 'без слэша'
@app.route('/lab2/a/')
def a2():
    return 'со слэшем'

flower_list = ['роза', 'тюльпан', 'незабудка', 'ромашка']
@app.route('/lab2/flowers/<int:flower_id>')
def flowers(flower_id):
    if flower_id >= len(flower_list):
        return "такого цветка нет", 404
    else:
        return "цветок: " + flower_list[flower_id]

@app.route('/lab2/add_flower/<name>')
def add_flower(name):
    if not name:
        return "Вы не задали имя цветка", 400
    flower_list.append(name)
    return f'''
<!doctype html>
<html>
    <body>
    <h1>Добавлен новый цветок</h1>
    <p>Название нового цветка: {name} </p>
    <p>Всего цветов: {len(flower_list)}</p>
    <p>Полный список: {flower_list}</p>
    <a href="/lab2/flowers">Посмотреть все цветы</a>
    </body>
</html>
'''

@app.route('/lab2/flowers')
def show_all_flowers():
    return f'''
<!doctype html>
<html>
    <body>
    <h1> Все цветы </h1>
    <p> Всего цветов: {len(flower_list)} </p>
    <ul>
        {"".join(f"<li>{flower}</li>" for flower in flower_list)}
    </ul>
    <a href="/lab2/clearflowers">Очистить список цветов</a>
    </body>
</html>
'''

@app.route('/lab2/clearflowers')
def clear_flowers():
    flower_list.clear()  
    return '''
<!doctype html>
<html>
    <body>
    <h1> Список цветов полностью очищен </h1>
    <a href="/lab2/flowers">Посмотреть все цветы</a>
    </body>
</html> 
'''

@app.route('/lab2/example')
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
    return render_template('example.html', name=name, course=course, laba=laba, 
                           group=group, fruits=fruits)

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/filters')
def filters():
    phrase = "О <b>сколько</b> <u>нам</u> <i>открытий</i> чудных..."
    return render_template('filter.html', phrase = phrase)

@app.route('/lab2/calc/<int:a>/<int:b>')
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

@app.route('/lab2/calc/')
def redirect_to_default():
    return redirect('/lab2/calc/1/1')

@app.route('/lab2/calc/<int:a>')
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
@app.route('/lab2/books')
def show_books():
    return render_template('books.html', books=book_spisok)

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
@app.route('/lab2/dogs')
def show_dogs():
    return render_template('dogs.html', dogs=dogs)