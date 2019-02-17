# song-retrieval.py
#
# Handles retrival of songs and lyrics


import requests
import re
import time
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz
from analytics.common_words import CommonWords
from analytics.release_history import ReleaseHistory
from analytics.song_number import SongNumber



artist = "slaughter beach, dog"

access_token = '8ufzdCrKWOB3Gfgx6VJgenQt531yP7KGHM4tk_3u3LD7xA0J1nexqUnHgH5LJjPD'

def get_artist_id(artist_name: str) -> int:
    """Gets the artist's id from Genius

    Args:
        artist_name: Artist's name

    Returns:
        int: Artist Genius id
    """

    # build and send search request to genius api
    base_url = 'https://api.genius.com'
    headers = {'Authorization': f'Bearer {access_token}'}
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
    headers = {'Authorization': f'Bearer {access_token}'}
    search_url = f'{base_url}/artists/{id}/songs?per_page=50'
    response = requests.get(search_url, headers=headers)
    
    json = response.json()
    url_list = []
    title_list = []
    for song in json['response']['songs']:
        if song['primary_artist']['id'] != id:
            continue
        title = song['title']
        if not (duplicate_title(title_list, title)):
            title_list.append(title)
            url_list.append(song['url'])
    return url_list

def duplicate_title(title_list: list, title: str) -> bool:
    """Checks if the given title is already in the list, based on string similaritys

    Args:
        title_list: List of titles
        title: Title we're checkint to see if there is a duplicate

    Returns:
        Bool representing whether the title is a dublicate or not
    """
    for t in title_list:
        if fuzz.token_set_ratio(t, title) > 90:
            return True
    return False

def scrape_lyrics(url: str) -> list:
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
    lyrics = re.sub(r'[().?:,!]', '', lyrics)

    # split up by spaces into a list
    lyrics = lyrics.lower().split(" ")

    # remove the unneccessary words and return the finalized lyrics
    return remove_unneccessary_words(lyrics)

def remove_unneccessary_words(lyrics: list) -> list:
    """ Removes words that are irrelevant to analytics

    Args:
        lyrics: list of all words in lyrics of a song
    
    Return:
        Lyrics with unneccesary words removed
    """

    # list of words we want to remove
    words = ['', 'the', 'i', 'a', 'an', 'of', 'with', 'at', 'from', 'into', 'and',
        'or', 'but', 'so', 'for', 'yet', 'as', 'because', 'since', 'this', 'that',
        'these', 'those', 'in', 'to', 'on', 'all', 'you', 'my', 'it', 'me', 'your',
        'when', 'out', 'up', 'be', 'is', 'if']

    return list(set(lyrics) - set(words))

    

#Tests

"""
print(get_artist_id(artist))
songs = get_song_url_list(get_artist_id(artist))


lyric_list = []
for song in songs:
    lyric_list.append(scrape_lyrics(song))

print(lyric_list[1])

#test = SongNumber(lyric_list).analyze()
#print(test)

print()
"""
#TODO remove this eventually
def main():
    # retrieve artist id
    id = get_artist_id(artist)
    # get artist's song urls
    song_urls = get_song_url_list(id)

    # for each song url, scrape the lyrics and append it to our lyric list
    lyric_list = []

    start = time.time()
    for url in song_urls:
        lyric_list.append(scrape_lyrics(url))
    end = time.time()

    print(f"Time to scrape all lyrics: {end-start}")

    # start = time.time()
    # print(CommonWords(lyric_list=lyric_list).analyze())
    # end = time.time()
    # print(f"Time to find most common words: {end-start}")
    ReleaseHistory(url_list=song_urls).analyze()

main()