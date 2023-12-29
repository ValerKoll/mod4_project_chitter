import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import User_repository
#..from post
#..from post_repository


app = Flask(__name__)


# Create a new Flask app
app = Flask(__name__)
# ======== routes =============
#
@app.route('/', methods=['GET'])
def get_emoji():
    return render_template('emoji.html', emoji=':)')

@app.route('/albums', methods=['GET'])
def get_albums():
    #arg1 = request.args['all']
    #sub_connection = get_flask_database_connection(app)
    #albums_repo = AlbumRepository(sub_connection)
    #albums = albums_repo.all()
    #text_to_return = [f"Title: {album.title}\nReleased: {album.release_year}"  for album in albums]
    #text_to_return = text_to_return[0] + text_to_return[1]
    #print(albums)
    return render_template('albums.html', users=users)

@app.route('/albums', methods=['POST'])
def add_album():
    #title = request.form['title']
    #release_year = request.form['release_year']
    #artist_id = request.form['artist_id']
    #sub_connection = get_flask_database_connection(app)
    #repo = AlbumRepository(sub_connection)
    #repo.create(Album(1, title, release_year, artist_id))
    #albums = repo.all()
    #response = ""
    #for album in albums:
    #    response += f"{album}\n"
    return response

#[...]

#
# ======== end rooutes ========


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))