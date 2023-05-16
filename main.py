from flask import Flask, redirect,render_template,request,url_for

app = Flask("__name__")



@app.route("/")
def main():
    return render_template("com_login.html")

@app.route("/dash")
def home():
    return render_template("dashboard.html")

@app.route("/login")
def login():
    return render_template("com_login.html")

@app.route("/register")
def register():
    return render_template("com_register.html")

@app.route("/user_login")
def user():
    return render_template("user_login.html")


if __name__ == "__main__":
    app.run(debug=True)