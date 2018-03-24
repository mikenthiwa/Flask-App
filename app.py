from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Rent')
def Rent():
    return render_template('Rent.html')

@app.route('/Profile')
def Profile():
    return render_template('Profile.html')

@app.route('/History')
def History():
    return render_template('History.html')

@app.route('/Log In')
def log_in():
    return render_template('Log In.html')

@app.route('/Sign Up')
def sign_up():
    return render_template('Sign Up.html')

if __name__ == '__main__':
    app.run(debug=True)