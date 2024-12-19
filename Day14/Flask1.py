
from flask import Flask, render_template, request, redirect, url_for

appLogin = Flask(__name__)

print(appLogin)
#step 2:create a route for the login page
@appLogin.route('/')
def login():
    return render_template('login.html')
#step3: create a route to handle the login form submission
@appLogin.route('/login',methods = ['POST'])
def handle_login():
    username = request.form['username']
    password = request.form['password']
    #step4: simple username and password authentication
    if username == "admin" and password == "password":
        #return f"Welcome. {username}!"
        return redirect(url_for ('show_dashboard'))

    else:
        return "Invalid credentials. Please try again."

@appLogin.route('/dashboard')
def show_dashboard():
    return render_template("dashboard.html")
if __name__ =="__main__":
    appLogin.run(port=8000,debug =True)