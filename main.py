from flask import Flask, render_template

app = Flask(__name__)

#Rotas e metodos aceitos
@app.route('/', methods=['GET'])
def ola_mundo():
    return render_template('index.html')

@app.route("/sobre")
def pagina_sobre():
    return render_template('/sobre.html')




app.run(debug=True)