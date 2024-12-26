from flask import Blueprint, render_template, redirect, request, session, current_app
from db import db
from db.models import users, articles
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy import or_
lab9 = Blueprint('lab9', __name__)
@lab9.route('/lab9/')
def lab():
    return render_template('lab9/index.html')