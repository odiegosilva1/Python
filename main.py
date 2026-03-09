from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
   if request.method == "POST": 
    nome = request.form['nomeForm']
    email = request.form['emailForm']
    print(f"Nome: {nome}")
    print(f"email: {email}")
    return render_template('formulario.html')


if __name__ == '__main__':
    app.run(debug=True)