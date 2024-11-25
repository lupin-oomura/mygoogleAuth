import os
from flask import Flask, redirect, url_for, render_template
import flask_login
from mygoogleAuth import mygoogleAuth

# Flask アプリのセットアップ
app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your_secret_key')

# mygoogleAuth のセットアップ
google_auth = mygoogleAuth("callback") #例：subfolder.callback
google_auth.setup_login_manager(app, "userinfo.json")
google_auth.load_users()

# ルートページ
@app.route("/")
def index():

    if flask_login.current_user.is_authenticated :
        print(f"access: {flask_login.current_user.name} - {flask_login.current_user.id} - {flask_login.current_user.email}")
        google_auth.save_users()

    return render_template('index.html')

# ログインルート
@app.route("/login")
def login():
    return google_auth.login()

# コールバックルート
@app.route("/login/callback")
def callback():
    user, error = google_auth.callback()
    if error:
        return error, 400

    # ユーザーをログイン
    flask_login.login_user(user)
    return redirect(url_for("index"))

# ログアウトルート
@app.route("/logout")
@flask_login.login_required
def logout():
    google_auth.logout()
    flask_login.logout_user()
    return redirect(url_for("index"))

# サブページのルート
@app.route("/subpage")
@flask_login.login_required
def subpage():
    return render_template('subpage.html')

if __name__ == "__main__":
    app.run(ssl_context="adhoc")  # 開発中は自己署名証明書を使用 (httpsにしないとGoogleAuthが通らない)
