from flask import Flask, Response

app = Flask(__name__)


@app.route("/")
def home():
    return Response("Hello Fizi", status=200, mimetype='text/plain')


if __name__ == "__main__":
    app.run()
