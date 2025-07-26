from flask import Flask, render_template, request  # removed unused imports

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'admin':
        return f"<h2>Welcome, {username}!</h2>"
    else:
        return "<h2>Login Failed. Please try again.</h2>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
