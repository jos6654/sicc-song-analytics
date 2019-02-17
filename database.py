import mysql.connector

db = mysql.connector.connect(host='localhost', user='root', passwd='Cc20178452#1')
cursor = db.cursor()
cursor.execute("USE songDatabase")


def insert_artist(artist_id: str, data: dict):
    sql = "DELETE FROM artist WHERE artistID = %s"
    val = (artist_id,)
    cursor.execute(sql, val)
    db.commit()
    sql = "INSERT INTO artist VALUES (%s, %s, %s, %s, %s, %s)"
    val = (artist_id, data['name'], data['releaseHistory'], data['commonWord'], data['sizeVocab'],
           data['numSongs'])
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, "record added to ARTIST")


def get_artist(artist_id: str):
    sql = "SELECT * FROM artist WHERE artistID = %s"
    val = (artist_id,)
    cursor.execute(sql, val)
    artist = []
    result = cursor.fetchall()
    for a in result:
        artist.append(a)
    return artist


def check_artist(artist_id: str):
    sql = "SELECT artistID FROM artist WHERE artistID = %s"
    val = (artist_id,)
    cursor.execute(sql, val)
    print(cursor.fetchall())
    if cursor.rowcount == 0:
        result = False
    else:
        result = True
    return result

