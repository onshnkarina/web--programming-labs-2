from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
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

        <footer>
            &copy; Онищенко Арина, ФБИ-24, 3 курс, 2024
        </footer>
    </body>
</html>
"""
