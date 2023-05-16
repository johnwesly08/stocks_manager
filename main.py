from flask import Flask, redirect,render_template,request,url_for
from flask_mysqldb import MySQL

app = Flask("__name__")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Pragathi@916'
app.config['MYSQL_DB'] = 'stocks'
app.secret_key="Resource_Control_And_Optimization_System"
mysql = MySQL(app)



@app.route("/")
def main():
    return render_template("com_login.html")

@app.route("/dash")
def home():
    return render_template("dashboard.html")

@app.route("/login")
def login():
    c_id = request.form['company_id']
    c_mail = request.form['business_email']
    c_pass = request.form['c_password']
    return render_template("com_login.html")

@app.route("/register", methods = ['POST','GET'])
def register():
    if request.method == 'POST':
        com_name = request.form['company_name']
        com_id = request.form['company_id']
        com_dir = request.form['director']
        com_pass = request.form['set_password']
        com_mail = request.form['business_email']
        com_country = request.form['country']
        com_state = request.form['state']
        con = mysql.connection.cursor()
        con.execute("INSERT INTO companies (Company_Name, Company_ID, Director, Company_Password, Business_Email, Country, State) VALUES (%s,%s,%s,%s,%s,%s,%s)",(com_name,com_id,com_dir,com_pass,com_mail,com_country,com_state))
        con.connection.commit()
        con.close()
        return redirect(url_for('/login'))
    return render_template("com_register.html")

@app.route("/user_login")
def user():
    return render_template("user_login.html")


if __name__ == "__main__":
    app.run(debug=True)