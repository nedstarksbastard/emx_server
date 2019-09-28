from flask import Flask, Response, request

app = Flask(__name__)


@app.route("/")
def home():

    answer = {
        "Ping": "OK",
        "Phone": "6463543951",
        "Degree": "Master of Science",
        "Position": "Data Pipeline Engineer",
        "Name": "Fizi Yadav",
        "Puzzle": "NA",
        "Referrer": "LinkedIn",
        "Source": "https://github.com/nedstarksbastard/emx_server/blob/master/emx_server.py",
        "Resume": "NA",
        "Status": "Yes (H1B)",
        "Years": "10+",
        "Email Address": "fizi@outlook.com"
    }

    question = request.args.get("q").title()
    return Response(answer[question], status=200, mimetype='text/plain')


if __name__ == "__main__":
    app.run()
