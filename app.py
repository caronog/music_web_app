import os
from lib.album import Album
from lib.artist import Artist
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
from flask import Flask, request
from lib.database_connection import get_flask_database_connection

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods=['POST'])
def create_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(
        None, 
        request.form['title'], 
        request.form['release_year'], 
        request.form['artist_id']
        )
    repository.add_album(album)
    return ""

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    return '\n'.join([str(album) for album in repository.all()])

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    return ', '.join(repository.all())

@app.route('/artists', methods=['POST'])
def create_artist():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(
        None,
        request.form['name'],
        request.form['genre']
    )
    repository.create(artist)
    return ''

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))

