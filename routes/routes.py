from flask import Blueprint, render_template

routes_bp = Blueprint('routes', __name__)


@routes_bp.route('/dashboard/home.html')
def dashboard_home():
    return render_template('dash/home.html')


@routes_bp.route('/dashboard/code.html')
def dashboard_code():
    return render_template('dash/chat.html')

@routes_bp.route('/dashboard/chat.rocket.html')
def dashboard_rocket():
    return render_template('dash/rocket.html')
