import mysql.connector

db_username = "DATABASE USERNAME HERE"
db_password = "DATABASE PASSWORD HERE"

db = mysql.connector.connect(host='localhost', user=db_username, password=db_password, auth_plugin='mysql_native_password')
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
    artist = { }
    temp = []
    result = cursor.fetchall()
    artist["name"] = result[0][1]
    artist["releaseHistory"] = result[0][2]
    artist["commonWord"] = result[0][3]
    artist["sizeVocab"] = result[0][4]
    artist["numSongs"] = result[0][5]
    return artist


def check_artist(artist_id: str):
    sql = "SELECT artistID FROM artist WHERE artistID = %s"
    val = (artist_id,)
    cursor.execute(sql, val)
    cursor.fetchall()
    if cursor.rowcount == 0:
        result = False
    else:
        result = True
    return result

