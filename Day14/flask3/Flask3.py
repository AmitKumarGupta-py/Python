from flask import Flask, render_template, request,redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/surveypage')
def survey():
    return render_template('survey.html')

@app.route('/result', methods=['POST'])
def result():
    favorite_music = request.form.getlist('music')
    return render_template('result.html', favorite_music=favorite_music)


if __name__ == '__main__':
    app.run(port = 5000,debug=True)
