from flask import Flask, Response, request
from utils.puzzle_handler import solve_puzzle

app = Flask(__name__)


@app.route("/")
def home():

    answer = {
        "Ping": "OK",
        "Phone": "6463543951",
        "Degree": "Master of Science",
        "Position": "Data Pipeline Engineer",
        "Name": "Fizi Yadav",
        "Referrer": "LinkedIn",
        "Source": "https://github.com/nedstarksbastard/emx_server/blob/master/emx_server.py",
        "Resume": "http://www.undg.net/resume",
        "Status": "Yes (H1B)",
        "Years": "10+",
        "Email Address": "fizi@outlook.com"
    }

    question = request.args.get("q").title()
    if question == "Puzzle":
        return Response(solve_puzzle(request.args.get("d")), status=200, mimetype='text/plain')
    else:
        return Response(answer[question], status=200, mimetype='text/plain')


if __name__ == "__main__":
    app.run()
