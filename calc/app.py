# Put your app in here.
from flask import Flask, request 
from operations import add, sub, mult, div

app = Flask(__name__)

# add route (add) 
@app.route('/add') 
def math_add():
    """Returns the sum of the query parameters"""
    # request.args['a'] as int 
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{add(a,b)}'

# add route (sub) 
@app.route('/sub')
def math_sub():
    """Returns the difference between the query parameters"""
    # request.args['a'] as int 
    a = int(request.args['a'])
    b = int(request.args['b'])
    return f'{sub(a,b)}'

# add route (mult)
@app.route('/mult')
def math_mult():
    """Returns the product of the query parameters"""
    # request.args['a'] as int 
    a = int(request.args['a'])
    b = int(request.args['b']) 
    return f'{mult(a,b)}'

# add route (div) 
@app.route('/div') 
def math_div():
    """Returns the quotient of the query parameters""" 
    # request.args['a'] as int 
    a = int(request.args['a'])
    b = int(request.args['b']) 
    return f'{div(a,b)}'