import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import User_repository
from lib.post import Post
from lib.post_repository import Post_repository
#..from post
#..from post_repository


# Create a new Flask app
app = Flask(__name__)

#init USER TEMP VAR to - assign None or current user
class testUser():
    id = None

current_user = testUser
current_user.id = None


# ==== Home Page - routes
#
#   current_active_user: None or username
#   index_section_id: None = see recent post
#                     current_user_posts = see user only post
# 
@app.route('/', methods=['GET'])
def index():
    return redirect('/index')

@app.route('/<home_page_section>', methods=['GET'])
def index_subsection(home_page_section):
    _connection = get_flask_database_connection(app)
    post_repository = Post_repository(_connection)
    if home_page_section == 'current_user_posts' and current_user.id:
        rows = post_repository.find(current_user.id)
    else:
        rows = post_repository.all()
    data = {
        'current_active_user': current_user.id,
        'home_page_section': home_page_section,
        'post_list': rows
    }
    return render_template('index.html', data=data)


# ==== Account Page - routes
#
#   current_active_user: None or username
#   GET arg: login
#             register
# 
@app.route('/account/<section>', methods=['GET'])
def login(section):
    if any([
        (section == 'login' and current_user.id == None),
        section == 'register'
        ]):
        return render_template('account.html', login_status=section)
    if section == 'logout' and current_user.id:
        current_user.id = None
        return redirect('/')


# ==== User login/register Form
#
#   current_active_user: None or username
#   POST arg: login
#             register
#     
@app.route('/user/<section>', methods=['POST'])
def user(section):
    _connection = get_flask_database_connection(app)
    post_repository = Post_repository(_connection)
    if section == 'login':
        username = request.form['username']
        password = request.form['passcode']
        current_user.id = post_repository.login(username, password)
        # --->>> store info in cookies
    elif section == 'register':
        name = request.form['name']
        username = request.form['username']
        password = request.form['passcode']
        current_user.id = id
        # --->>> store info in cookies
        # ---->>>>   create user
    return redirect('/')






#  to be continued

# @app.route('/query', methods=['GET', 'POST'])
# def get_query():
#     if request.method == 'GET':
#         return render_template('test.html', data={'id':1,'name':2})
#     elif request.method == 'POST':
#         return render_template('test.html')

# app.route('/query/<id>', methods=['POST'])
# def post_query():
#     arg1 = request.form['id']
#     return redirect('/index.html') 
    #return render_template("/test", users=arg1)

"""
@app.route('/login', methods=['GET'])
def get_users():
    arg1 = request.args['all']
    #sub_connection = get_flask_database_connection(app)
    #albums_repo = AlbumRepository(sub_connection)
    #albums = albums_repo.all()
    #text_to_return = [f"Title: {album.title}\nReleased: {album.release_year}"  for album in albums]
    #text_to_return = text_to_return[0] + text_to_return[1]
    #print(albums)
    users = "111"
    return render_template('users.html', users=users)
@app.route('/login', methods=['POST'])
def post_users():
    arg1 = request.form['id_text']
    arg2 = request.form['id']
    #sub_connection = get_flask_database_connection(app)
    #albums_repo = AlbumRepository(sub_connection)
    #albums = albums_repo.all()
    #text_to_return = [f"Title: {album.title}\nReleased: {album.release_year}"  for album in albums]
    #text_to_return = text_to_return[0] + text_to_return[1]
    #print(albums)
    users = arg1
    return render_template('users.html', users=users)
"""

"""
@app.route('/users', methods=['POST'])
def add_user():
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
"""
#[...]

#
# ======== end rooutes ========


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))