from flask import Blueprint, render_template, request, abort
from datetime import datetime
lab7 = Blueprint('lab7', __name__)
@lab7.route('/lab7/')
def main():
    return render_template('lab7/lab7.html')

films = [
    {
        'title': 'Inception',
        'title_ru': 'Начало',
        'year': 2010,
        'description': 'Кристофер Нолан подарил миру интеллектуальный триллер о \
            мире снов. Главный герой Доминик Кобб (Леонардо ДиКаприо) — профессионал \
            по внедрению идей в подсознание. Ему нужно выполнить невозможное задание: \
            внедрить идею в сознание человека, чтобы спасти свою жизнь. Фильм поражает\
            сложностью сюжета, визуальными эффектами и философскими размышлениями о реальности.'
    },
    {
        'title': 'Interstellar',
        'title_ru': 'Интерстеллар)',
        'year': 2014,
        'description': 'Фильм Нолана о спасении человечества. Земля умирает, и группа исследователей \
            отправляется в путешествие через червоточину в другой галактике, чтобы найти новый дом для людей. Фильм \
            поражает глубиной сюжета, научными идеями и эмоциональной историей отца и дочери.'

    },
    {
        'title': "The Matrix",
        'title_ru': 'Матрица',
        'year': 1999,
        'description': 'Кинопрорыв, который изменил жанр. Главный герой Нео (Киану Ривз) узнает, что реальность — это \
            симуляция, созданная машинами. Он присоединяется к борцам за свободу, чтобы освободить человечество. Фильм \
            знаменит своими философскими идеями, крутыми боями и культовыми кадрами.'
    },
    {
        'title': "Fight Club",
        'title_ru': 'Бойцовский клуб',
        'year': 1999,
        'description': 'Дэвид Финчер снял культовый фильм по роману Чака Паланика. Главный герой (Эдвард Нортон) встречает Тайлера \
            Дёрдена (Брэд Питт), который вдохновляет его на создание подпольного клуба драки. Фильм знаменит своим разочарованием в \
            потребительском обществе и культовым финалом.'
    },
    {
        'title': 'Guardians of the Galaxy',
        'title_ru': 'Стражи Галактики',
        'year': 2014,
        'description': 'Джеймс Ганн подарил Marvel комедийный экшен о группе неформальных героев, которые защищают Вселенную. Фильм \
            знаменит своим юмором, саундтреком 70-х и динамичным действием.'
    }
]
@lab7.route('/lab7/rest-api/films/', methods=['GET'])
def get_films():
    return films
@lab7.route('/lab7/rest-api/films/<int:id>', methods=['GET'])
def get_film(id):
    if 0 <= id < len(films):
        return films[id]
    else:
        abort(404)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['DELETE'])
def del_film(id):
    if 0 <= id < len(films):
        del films[id]
        return '', 204
    else:
        abort(404)

@lab7.route('/lab7/rest-api/films/<int:id>', methods=['PUT'])
def put_film(id):
    if 0 <= id < len(films):
        film = request.get_json() 
        if film.get('description', '') == '':
            return {'description': 'Заполните описание'}, 400
        elif len(film['description']) > 2000:
            return ({'description': 'Описание не должно превышать 2000 символов'}), 400
        if not film.get('title') and not film.get('title_ru'):
            return ({'title': 'Заполните поля с названиями'}), 400
        if not film.get('title_ru'):
            return ({'title_ru': 'Заполните русское название'}), 400
        if film.get('title', '') == '':
            film['title'] = film['title_ru']
        if not film.get('year'):
            return ({'year': 'Укажите год выпуска фильма'}), 400
        elif not str(film['year']).isdigit() or int(film['year']) < 1895 or int(film['year']) > 2100:
            return ({'year': 'Введите корректный год (1895-2100)'}), 400
        films[id] = film
        return films[id]
    else:
        abort(404)

@lab7.route('/lab7/rest-api/films/', methods=['POST'])
def add_film():
    film = request.get_json()
    if not film:
        abort(404)
    if film.get('description', '') == '':
        return {'description': 'Заполните описание'}, 400
    elif len(film['description']) > 2000:
        return ({'description': 'Описание не должно превышать 2000 символов'}), 400
    if not film.get('title') and not film.get('title_ru'):
        return ({'title': 'Заполните поля с названиями'}), 400
    if not film.get('title_ru'):
        return ({'title_ru': 'Заполните русское название'}), 400
    
    if film.get('title', '') == '':
        film['title'] = film['title_ru']
    if not film.get('year'):
        return ({'year': 'Укажите год выпуска фильма'}), 400
    elif not str(film['year']).isdigit() or int(film['year']) < 1895 or int(film['year']) > 2100:
        return ({'year': 'Введите корректный год (1895-2100)'}), 400
    films.append(film)
    return {'id': len(films) - 1}, 201