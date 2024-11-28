from flask import Blueprint, render_template, redirect, request, session, current_app
lab6 = Blueprint('lab6', __name__)

offices =[]
for i in range (1, 11):
    offices.append({"number": i, "tenant": "", "price": 1000})

@lab6.route('/lab6/')
def lab():
    return render_template('lab6/lab6.html')

@lab6.route('/lab6/json-rpc-api/', methods=['POST'])
def api():
    data = request.json
    id = data['id']
    if data['method'] == 'info':
        total_cost = sum(office['price'] for office in offices if office['tenant'])
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
        for office in offices:
            if office['number'] == office_number:
                if office['tenant'] != '':
                    return {
                        'jsonrpc': '2.0', 
                        'error': {
                            'code': 2,
                            'message': 'Already'
                        },
                        'id': id
                    }
                office['tenant'] = login
                return {
                'jsonrpc': '2.0', 
                'result': 'success',
                'id': id
                }
    if data['method'] == 'cancellation':
        office_number = data['params']
        for office in offices:
            if office['number'] == office_number:
                if office['tenant'] != login:
                    return {
                        'jsonrpc': '2.0',
                        'error': {
                            'code': 3,
                            'message': 'Forbidden'
                        },
                        'id': id
                    }
                office['tenant'] = ''
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