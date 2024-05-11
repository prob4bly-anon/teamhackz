from flask import Blueprint, render_template, request, redirect, session
import requests
import json

login_bp = Blueprint('login', __name__)

# Load config
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# Get Discord section from config
discord_config = config['Discord']

@login_bp.route('/login')
def login_redirect():
    return redirect('https://discord.com/oauth2/authorize?client_id=269930857341517824&response_type=code&redirect_uri=http%3A%2F%2F127.0.0.1%3A8080%2Fcallback&scope=identify+email+guilds.join')

@login_bp.route('/callback')
def login():
    try:
        code = request.args.get('code')
        if code is not None:
            # Exchange the code for an access token
            token_url = 'https://canary.discord.com/api/oauth2/token'
            token_payload = {
                'client_id': discord_config['client_id'],
                'client_secret': discord_config['client_secret'],
                'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': discord_config['redirect_uri']
            }
            token_response = requests.post(token_url, data=token_payload)
            token_data = token_response.json()

            # Use the access token to fetch user details
            if 'access_token' in token_data:
                user_url = 'https://canary.discord.com/api/users/@me'
                headers = {
                    'Authorization': f'Bearer {token_data["access_token"]}'
                }
                user_response = requests.get(user_url, headers=headers)
                user_data = user_response.json()

                # Extract user details
                username = user_data.get('username')
                user_id = user_data.get('id')
                email = user_data.get('email')
                avatar = f'https://cdn.discordapp.com/avatars/{user_id}/{user_data["avatar"]}.png'

                # Redirect to the dashboard
                session['username'] = username
                session['email'] = email
                session['avatar_url'] = avatar
                session['user_id'] = user_id
                return redirect('/dashboard')
            else:
                return 'Failed to obtain access token.'
        else:
            return 'No value parameter provided in the URL.'
    except Exception as e:
        return f'An error occurred: {str(e)}'
