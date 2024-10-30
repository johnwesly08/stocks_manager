import os
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, url_for, flash
from flask_mysqldb import MySQL

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MySQL configurations from environment variables
app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER', 'root')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD', 'your_password_here')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB', 'stocks')
app.secret_key = os.getenv('SECRET_KEY', 'Resource_Control_And_Optimization_System')

mysql = MySQL(app)

@app.route("/")
def main():
    return render_template("com_login.html")

@app.route("/dash")
def home():
    return render_template("dashboard.html")

@app.route("/login", methods=['POST'])
def login():
    c_id = request.form['company_id']
    c_mail = request.form['business_email']
    c_pass = request.form['c_password']
    
    # Perform login logic here (query database to check credentials)
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM companies WHERE Company_ID = %s AND Business_Email = %s AND Company_Password = %s", (c_id, c_mail, c_pass))
    user = cur.fetchone()
    cur.close()

    if user:
        return redirect(url_for('home'))  # Redirect to dashboard on success
    else:
        flash("Invalid credentials, please try again.")
        return redirect(url_for('main'))

@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        com_name = request.form['company_name']
        com_id = request.form['company_id']
        com_dir = request.form['director']
        com_pass = request.form['set_password']
        com_mail = request.form['business_email']
        com_country = request.form['country']
        com_state = request.form['state']

        try:
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO companies (Company_Name, Company_ID, Director, Company_Password, Business_Email, Country, State) VALUES (%s,%s,%s,%s,%s,%s,%s)",
                        (com_name, com_id, com_dir, com_pass, com_mail, com_country, com_state))
            mysql.connection.commit()
            cur.close()
            return redirect(url_for('login'))
        except Exception as e:
            flash("An error occurred while registering the company: " + str(e))
            return redirect(url_for('register'))

    return render_template("com_register.html")

@app.route("/user_login")
def user():
    return render_template("user_login.html")

if __name__ == "__main__":
    app.run(debug=True)
