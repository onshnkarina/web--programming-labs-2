from flask import Blueprint, render_template, request, session, current_app
import psycopg2
from psycopg2.extras import RealDictCursor
from os import path
import sqlite3
lab6 = Blueprint('lab6', __name__)

def db_connect():
    if current_app.config['DB_TYPE'] == 'postgres':
        conn = psycopg2.connect(
            host='127.0.0.1',
            database='arina_onishchenko_knowledge_base',
            user='arina_onishchenko_knowledge_base',
            password='12345'
        )
        cur = conn.cursor(cursor_factory=RealDictCursor)
    else:
        dir_path = path.dirname(path.realpath(__file__))
        db_path = path.join(dir_path, "database.db")
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
    return conn, cur

def db_close(conn, cur):
    conn.commit()
    cur.close()
    conn.close()

@lab6.route('/lab6/')
def lab():
    return render_template('lab6/lab6.html')

@lab6.route('/lab6/json-rpc-api/', methods=['POST'])
def api():
    data = request.json
    id = data['id']

    conn, cur = db_connect()

    if data['method'] == 'info':
        cur.execute("SELECT * FROM offices")
        offices = cur.fetchall()
        cur.execute("SELECT SUM(price) AS total_cost FROM offices WHERE tenant IS NOT NULL")
        total_cost = cur.fetchone()['total_cost'] or 0
        db_close(conn, cur)
        return {
            'jsonrpc': '2.0',
            'result': {
                'offices': offices,
                'total_cost': total_cost
            },
            'id': id
        }
    login = session.get('login')
    if not login:
        db_close(conn, cur) 
        return {
            'jsonrpc': '2.0',
            'error': {
                'code': 1,
                'message': 'Unauthorized'
            },
            'id': id
        }
    if data['method'] == 'booking':
        office_number = data['params']
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("SELECT tenant FROM offices WHERE number = %s", (office_number,))
        else:
            cur.execute("SELECT tenant FROM offices WHERE number = ?", (office_number,))
        
        office = cur.fetchone()
        if office and office['tenant']:
            db_close(conn, cur)
            return {
                'jsonrpc': '2.0',
                'error': {
                    'code': 2,
                    'message': 'Already'
                },
                'id': id
            }
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("UPDATE offices SET tenant = %s WHERE number = %s", (login, office_number))
        else:
            cur.execute("UPDATE offices SET tenant = ? WHERE number = ?", (login, office_number))
        
        db_close(conn, cur)
        return {
            'jsonrpc': '2.0',
            'result': 'success',
            'id': id
        }
        
    if data['method'] == 'cancellation':
        office_number = data['params']
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("SELECT tenant FROM offices WHERE number = %s", (office_number,))
        else:
            cur.execute("SELECT tenant FROM offices WHERE number = ?", (office_number,))
        
        office = cur.fetchone()
        if office and office['tenant'] != login:
            db_close(conn, cur)
            return {
                'jsonrpc': '2.0',
                'error': {
                    'code': 3,
                    'message': 'Forbidden'
                },
                'id': id
            }
        if current_app.config['DB_TYPE'] == 'postgres':
            cur.execute("UPDATE offices SET tenant = NULL WHERE number = %s", (office_number,))
        else:
            cur.execute("UPDATE offices SET tenant = NULL WHERE number = ?", (office_number,))
        
        db_close(conn, cur)
        return {
            'jsonrpc': '2.0',
            'result': 'success',
            'id': id
        }
    return {
        'jsonrpc': '2.0', 
        'error': {
            'code': -32601,
            'message': 'Method not found'
        },
        'id': id
    }
