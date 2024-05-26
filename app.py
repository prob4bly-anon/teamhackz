#!/usr/bin/python3
from dotenv import load_dotenv
load_dotenv() 
from datetime import timedelta
import os

import eventlet
eventlet.monkey_patch() # Call before other modules are imported, or else it throws a error:)


from flask import Flask, redirect, render_template, session
from flask_socketio import SocketIO, emit
from routes.index import index_bp
from routes.login import login_bp
from routes.routes import routes_bp
from routes.dash import dash_bp
from routes.livechat import chat_bp

app = Flask(__name__)
socketio = SocketIO(app, async_mode='eventlet')

# Registering the blueprint
app.register_blueprint(index_bp)
app.register_blueprint(login_bp)
app.register_blueprint(dash_bp)
app.register_blueprint(routes_bp)
app.register_blueprint(chat_bp)

app.secret_key = os.getenv('SECRET_KEY')
app.config['SESSION_COOKIE_HTTPONLY'] = True  
app.config['SESSION_COOKIE_SECURE'] = True  
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7) 

@socketio.on('connect')
def connect():
    emit('ready',  {'message':'Connected. Lets dance!!!', 'username': session['username']})

@socketio.on('message')
def handle_message(data):
    emit('messageReceive', {'username': data['username'], 'message': data['text']}, broadcast=True)

socketio.run(app, port=8080, 
        debug=True)
# In production:
#       pip install gunicorn
#       gunicorn --worker-class eventlet -w 1 app:app
#       debug = False