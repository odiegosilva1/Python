from flask import Flask

app = Flask(__name__)

#Rotas e metodos aceitos
@app.route('/', methods=['GET'])
def ola_mundo():
    return "Aee"

@app.route("/sobre")
def pagina_sobre():
    return "Sobre"




app.run(debug=True)