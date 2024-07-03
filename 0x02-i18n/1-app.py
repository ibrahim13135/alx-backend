from flask import Flask, render_template

from flask_babel import Babel


class Config:
    LANGUAGES = ["en", "fr"]
    #set Babel’s default locale ("en") and timezone ("UTC"
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app: Flask = Flask(__name__)

#configure Flask-Babel in your Flask application
app.config.from_object(Config)
bable = Babel(app)


@app.route('/')
def index() -> str:
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
