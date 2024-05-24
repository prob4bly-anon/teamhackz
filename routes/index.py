from flask import Blueprint, render_template, request
import re

index_bp = Blueprint('index', __name__)

@index_bp.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    if is_mobile(user_agent):
        return render_template('mobile/index.html')
    else:
        return render_template('pc/index.html')
    
@index_bp.route('/about')
def about():
    return render_template('/about.html')
    
@index_bp.route('/contact')
def contact():
    return render_template('/contact.html')

def is_mobile(user_agent):
    # Regular expression to match common mobile user agents
    mobile_regex = re.compile(r'android|iphone|ipod|ipad|windows phone|iemobile|blackberry|mobile', re.IGNORECASE)
    return mobile_regex.search(user_agent)
