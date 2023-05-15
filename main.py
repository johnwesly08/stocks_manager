from flask import Flask, redirect,render_template,request

app = Flask("__name__")



@app.route("/")
def signin():
    return render_template("com_login.html")


if __name__ == "__main__":
    app.run()