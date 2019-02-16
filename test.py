# song-retrieval.py
#
# Handles retrival of songs and lyrics


import requests
import re
from bs4 import BeautifulSoup


# TESTING VARIABLES
song = "uptown girl"
artist = "billy joel"

def get_artist_id(artist_name: str) -> int:
    """Gets the artist's id from Genius

    Args:
        artist_name: Artist's name

    Returns:
        int: Artist Genius id
    """

    # build and send search request to genius api
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + '8ufzdCrKWOB3Gfgx6VJgenQt531yP7KGHM4tk_3u3LD7xA0J1nexqUnHgH5LJjPD'}
    search_url = base_url + '/search'
    data = {'q': artist_name}
    response = requests.get(search_url, data=data, headers=headers)
    
    json = response.json()

    # loop through all hits in search
    for hit in json['response']['hits']:
        # if the artist we searched for is this hit, return the artist's id
        if artist.lower() in hit['result']['primary_artist']['name'].lower():
            return hit['result']['primary_artist']['id']


def get_song_url_list(id: int) -> list:
    """Gets list of urls of songs by an artist

    Args:
        id: Artist's Genius id

    Returns:
        list of song urls
    """

    # build and send search request to genius api
    base_url = 'https://api.genius.com'
    headers = {'Authorization': 'Bearer ' + '8ufzdCrKWOB3Gfgx6VJgenQt531yP7KGHM4tk_3u3LD7xA0J1nexqUnHgH5LJjPD'}
    search_url = f'{base_url}/artists/{id}/songs'
    response = requests.get(search_url, headers=headers)
    
    json = response.json()
    url_list = []
    for song in json['response']['songs']:
        url_list.append(song['url'])

    return url_list

def scrape_lyrics(url: str) -> str:
    """Gets the lyrics from a song's url

    Args:
        url: URL of song

    Returns:
        Lyrics modified to have no punctuation or excess whitespaces
    """

    page = requests.get(url)
    html = BeautifulSoup(page.text, "html.parser")
    lyrics = html.find('div', class_="lyrics").get_text()

    # capture all bracketed section of lyrics (ie: [Chorus], [Bridge], [Verse 1])
    # and replace with nothing
    lyrics = re.sub(r'\[[^\]]+\]', '', lyrics)
    
    # replace all series of whitespace with a single space
    lyrics = re.sub(r'\s+', ' ', lyrics)
    
    # remove all punctuation (beside apostrophe)
    lyrics = re.sub(r'[().?:,]', '', lyrics)
    
    print(lyrics)


"""
print(get_artist_id(artist))
songs = get_song_url_list(get_artist_id(artist))
scrape_lyrics( songs[0] )
"""