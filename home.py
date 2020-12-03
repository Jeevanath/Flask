from flask import Flask, render_template,request

app: Flask = Flask(__name__)

@app.route('/')
def login():
    return render_template("login.html")


@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/login_val', methods=['POST'])
def login_val():
    email    = request.form.get('email')
    password = request.form.get('password')
    if email == 'jeevanath1996@gmail.com' and password == 'jvnthny1':
        return home()

if __name__ == "__main__":
    app.run(debug=True)