from flask import Blueprint, render_template, redirect, request, session, url_for
from db import db
from db.models import users, articles
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import or_
from werkzeug.utils import secure_filename

lab9 = Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def lab():
    return render_template('lab9/index.html')

@lab9.route('/lab9/step1', methods=['GET', 'POST'])
def step1():
    if request.method == 'POST':
        session['name'] = request.form.get('name')
        return redirect(url_for('lab9.step2'))
    return render_template('lab9/step1.html')

@lab9.route('/lab9/step2', methods=['GET', 'POST'])
def step2():
    if request.method == 'POST':
        session['age'] = request.form.get('age')
        return redirect(url_for('lab9.step3'))
    return render_template('lab9/step2.html', name=session.get('name'))

@lab9.route('/lab9/step3', methods=['GET', 'POST'])
def step3():
    if request.method == 'POST':
        session['gender'] = request.form.get('gender')
        return redirect(url_for('lab9.step4'))
    return render_template('lab9/step3.html', name=session.get('name'), age=session.get('age'))

@lab9.route('/lab9/step4', methods=['GET', 'POST'])
def step4():
    if request.method == 'POST':
        session['preference1'] = request.form.get('preference1')
        return redirect(url_for('lab9.step5'))
    return render_template('lab9/step4.html', name=session.get('name'), age=session.get('age'), gender=session.get('gender'))

@lab9.route('/lab9/step5', methods=['GET', 'POST'])
def step5():
    if request.method == 'POST':
        session['preference2'] = request.form.get('preference2')
        return redirect(url_for('lab9.result'))
    preference1 = session.get('preference1')
    return render_template('lab9/step5.html', name=session.get('name'), age=session.get('age'), gender=session.get('gender'), preference1=preference1)

@lab9.route('/lab9/result')
def result():
    name = session.get('name')
    age = session.get('age')
    gender = session.get('gender')
    preference1 = session.get('preference1')
    preference2 = session.get('preference2')
    return render_template('lab9/result.html', name=name, age=age, gender=gender, preference1=preference1, preference2=preference2)