from flask import Blueprint, render_template, request, session, redirect

dash_bp = Blueprint('dash', __name__)

@dash_bp.route('/dashboard')
def index():
   if 'username' in session:
      pass
   else:
      return redirect('/login')
   
   username = session.get('username')
   avatar_url = session.get('avatar_url')
   email = session.get('email')
   user_id = session.get('user_id')
   return render_template('dash/dash.html', name=username)

@dash_bp.route('/dashboard/profile')
def user_profile():
   if 'username' in session:
      return {'message': "success", 'data': {'username': session['username'],'avatar_url': session['avatar_url']}}, 200
   else:
      return {'message': "404 Unauthorized ! | 1337 Lumino Haxxor"}, 404