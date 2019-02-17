from flask import Flask, render_template, request
import logging
from logging.handlers import RotatingFileHandler
import json
import song_retrieval
import database

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("%s.html" % "index")

@app.route('/analyze', methods=['POST'])
def analyze():
    #DEBUG
    app.logger.warning(request.get_json())
    app.logger.warning(type(request.get_json()))
    app.logger.warning(request.get_json()['artist'])

    # retrieve artist from request
    artist = request.get_json()['artist'].lower()

    # get artist id
    artist_id = (song_retrieval.get_artist_id(artist))

    app.logger.warning(artist_id)
    # check if the artist is already in the database
    if database.check_artist(artist_id):
        # if so, retrieve data and return
        artist_stats = database.get_artist(artist_id)
        #TODO format into json and return
        return "ARTIST IN DB"
    
    # otherwise run analytics
    song_retrieval.perform_analytics(int(artist_id), artist)


    #TODO:
    # request recieved, now we have to get artist ID
    # if artist id is in database, return stats
    # else, run analytics

    return "gottem"

if __name__ == '__main__':
    
    app.run(debug=True)
