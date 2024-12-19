from flask import Flask, render_template, request,redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ageform')
def ageform():
    return render_template('ageform.html')

@app.route('/result', methods=['POST'])
def result():
    name = request.form['name']
    age = int(request.form['age'])

    if age >= 18:
        result = f'Hello {name}, you are an adult.'
    else:
        result = f'Hello {name}, you are a minor.'

    return render_template('result.html', message=result)

if __name__ == '__main__':
    app.run(port = 5000,debug=True)
