from flask import Blueprint, render_template, session, redirect

chat_bp = Blueprint('livechat', __name__)

@chat_bp.route('/dashboard/chat')
def chat():
    if 'username' in session:
        return render_template('/livechat.html', username=session['username'])
    return redirect('/')
