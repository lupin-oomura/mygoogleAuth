import os
from flask import Flask, redirect, url_for, render_template
from flask_login import login_user, logout_user, login_required
from mygoogleAuth import mygoogleAuth

# Flask アプリのセットアップ
app = Flask(__name__)
# app.secret_key = os.getenv('FLASK_SECRET_KEY', 'your_secret_key')

# mygoogleAuth のセットアップ
google_auth = mygoogleAuth(app)

# ルートページ
@app.route("/")
def index():
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
    login_user(user)
    return redirect(url_for("index"))

# ログアウトルート
@app.route("/logout")
@login_required
def logout():
    google_auth.logout()
    logout_user()
    return redirect(url_for("index"))

# サブページのルート
@app.route("/subpage")
@login_required
def subpage():
    return render_template('subpage.html')

if __name__ == "__main__":
    app.run(ssl_context="adhoc")  # 開発中は自己署名証明書を使用 (httpsにしないとGoogleAuthが通らない)
