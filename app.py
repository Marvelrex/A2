
from flask import Flask,  render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')

@app.route('/basic')
def basicInfo():
    return render_template('BasicInfo.html')

@app.route('/contact')
def ContactMe():
    return render_template('ContactMe.html')

@app.route('/pets')
def Mypet():
    return render_template('MyPet.html')

@app.route('/project')
def Myprojects():
    return render_template('Myprojects.html')


if __name__ == '__main__':
    app.run()
