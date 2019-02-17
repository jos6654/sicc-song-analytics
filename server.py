from flask import Flask, render_template, request
import logging
from logging.handlers import RotatingFileHandler
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("%s.html" % "index")

@app.route('/analyze', methods=['POST'])
def analyze():

    app.logger.warning(request.get_json())

    #TODO:
    # request recieved, now we have to get artist ID
    # if artist id is in database, return stats
    # else, run analytics

    return "gottem"

if __name__ == '__main__':
    
    app.run(debug=True)
