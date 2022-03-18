import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <html>
    <head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>Егор гееей</title>
    </head>
    <body>
    <h1>Заголовок</h1>
    <p><img src="https://github.com/Peteryarusov/Flaskyl/blob/master/dzen.jpg" alt="Письма мастера дзен"></p>
    </body>
    </html>"""


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)