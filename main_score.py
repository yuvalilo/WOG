from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE
from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def score_server():
    if os.path.exists(SCORES_FILE_NAME):
        score = open(SCORES_FILE_NAME).readline()
        return f"""
            <html> 
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>The score is:</h1>
                    <div id="score">{score}</div>
                </body>
            </html> """
    else:
        return f"""
            <html> 
                <head>
                    <title>Scores Game</title>
                </head>
                <body>
                    <h1>ERROR:</h1>
                    <div id="score" style="color:red">{BAD_RETURN_CODE}</div>
                </body>
            </html> """


app.run("0.0.0.0", port=5000)
