from flask import Flask

app = Flask(__name__)


# Rora raiz
@app.route('/')
def index():
    return('Olá mowdoo')

if __name__ == '__main__':
    app.run()