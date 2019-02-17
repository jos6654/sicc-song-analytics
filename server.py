from flask import Flask, render_template, request
import logging
from logging.handlers import RotatingFileHandler
import json
import song_retrieval

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("%s.html" % "index")

@app.route('/analyze', methods=['POST'])
def analyze():
    #DEBUG
    app.logger.warning(request.get_json())

    # retrieve artist from request
    artist = request.get_json()['artist']
    
    if song_retrieval.get_artist_id(artist)

    #TODO:
    # request recieved, now we have to get artist ID
    # if artist id is in database, return stats
    # else, run analytics

    return "gottem"

if __name__ == '__main__':
    
    app.run(debug=True)
