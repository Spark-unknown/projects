from flask import Flask, redirect, url_for, session, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
import requests
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Set up Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Replace with your own Google Client ID and Secret
CLIENT_ID = 'fluted-century-437405-q3'
CLIENT_SECRET = 'YOUR_GOOGLE_CLIENT_SECRET'
REDIRECT_URI = 'http://localhost:5000/callback'

class User(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route('/')
def index():
    return 'Welcome to the Google Auth Demo! <a href="/login">Login with Google</a>'

@app.route('/login')
def login():
    return redirect(
        f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=email"
    )

@app.route('/callback')
def callback():
    code = request.args.get('code')
    
    # Exchange code for access token
    token_url = 'https://oauth2.googleapis.com/token'
    token_data = {
        'code': code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code',
    }
    
    token_r = requests.post(token_url, data=token_data)
    token_json = token_r.json()
    
    # Use the access token to get user information
    user_info_url = 'https://www.googleapis.com/oauth2/v2/userinfo'
    headers = {'Authorization': f"Bearer {token_json['access_token']}"}
    user_info = requests.get(user_info_url, headers=headers).json()
    
    # Create user and login
    user = User(user_info['email'])
    login_user(user)
    
    return jsonify(user_info)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/protected')
@login_required
def protected():
    return 'This is a protected route.'

if __name__ == '__main__':
    app.run(debug=True)
