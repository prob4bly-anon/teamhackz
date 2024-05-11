# main.py
from flask import Flask
from routes.index import index_bp
from routes.login import login_bp
from routes.routes import routes_bp
from routes.dash import dash_bp


app = Flask(__name__)

# Registering the blueprint
app.register_blueprint(index_bp)
app.register_blueprint(login_bp)
app.register_blueprint(dash_bp)
app.register_blueprint(routes_bp)

app.secret_key = 'hackz6966'

