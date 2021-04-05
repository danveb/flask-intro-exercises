from flask import Flask, request 

app = Flask(__name__)

# Add route 
@app.route('/welcome') 
def welcome():
    """Returns the message welcome"""
    return 'Welcome' 

# Add route 
@app.route('/welcome/<message>')
def welcome_msg(message):
    """Returns custom message"""
    return f'Welcome {message}'
