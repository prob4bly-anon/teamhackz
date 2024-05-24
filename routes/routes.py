from flask import Blueprint, render_template, session, redirect

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/dashboard/home')
def dashboard_home():
    if session:
        return render_template('dash/home.html')
    return redirect('/')

