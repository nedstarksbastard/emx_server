from flask import Flask, Response, request

app = Flask(__name__)


@app.route("/")
def home():

    answer = {
        "Ping": "OK",
        "Phone": "6463543951",
        "Degree": "Master of Science",
        "Position": "Data Pipeline Engineer",
        "Name": "Fizi Yadav"
    }

    question = request.args.get("q").title()
    return Response(answer[question], status=200, mimetype='text/plain')


if __name__ == "__main__":
    app.run()
