from flask import Blueprint, url_for, redirect
lab1 = Blueprint('lab1',__name__)

@lab1.route("/index")
def start():

    return redirect("/menu", code=302)


@lab1.route("/lab1")
def lab():

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


@lab1.route('/lab1/oak')
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


@lab1.route('/lab1/student')
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


@lab1.route('/lab1/python')
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


@lab1.route('/lab1/autumn')
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

 