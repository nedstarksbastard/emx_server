from flask import Flask, Response, request
from utils.puzzle_handler import solve_puzzle

app = Flask(__name__)


@app.route("/")
def home():

    answers = {
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

    question = request.args.get("q")
    if not question:
        return Response("malformed request", status=400, mimetype='text/plain')
    elif question.title() == "Puzzle":
        resp = solve_puzzle(request.args.get("d"))
        return Response(resp if resp else "Malformed puzzle string", status=200 if resp else 400, mimetype='text/plain')
    elif question not in answers:
        return Response("malformed request", status=400, mimetype='text/plain')
    else:
        return Response(answers[question.title()], status=200, mimetype='text/plain')


if __name__ == "__main__":
    app.run()
