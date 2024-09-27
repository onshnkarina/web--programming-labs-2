from flask import Flask, redirect
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

        <div>
            <a href='http://127.0.0.1:5000/lab1'>Лабораторная работа 1</a>
        </div>

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

        <footer>
            &copy; Онищенко Арина, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""