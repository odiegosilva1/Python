from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape

app = Flask(__name__)
app.config['SQLAMCHEMY_DATABASE_URI']





if __name__ == '__main__':
    app.run(debug=True)