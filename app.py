import os, copy
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

### store current logged in user - assign None or current user
# next phase:  implement cookies
#
#  list representing USER: [ID, NAME]
NULL_USER = User(None, None, None, None)
active_user = copy.copy(NULL_USER)
#
########################

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
    global active_user      #to be replaced with cookies
    _connection = get_flask_database_connection(app)
    post_repository = Post_repository(_connection)
    if home_page_section == 'current_user_posts' and active_user.is_valid():
        rows = post_repository.find(active_user.id)
    else:
        rows = post_repository.all()
    data = {
        'active_user_id': active_user.id,
        'active_user_name': active_user.name,
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
    global active_user      #to be replaced with cookies
    if all([not(active_user.is_valid()) and
            any([
                section == 'login',
                section == 'register'
                ])
            ]):
        return render_template('account.html', login_status=section)
    elif all([
        section == 'logout',
        active_user.is_valid()
        ]):
        active_user = copy.copy(NULL_USER)
    return redirect('/')


# ==== User login/register Form
#
#   active_user: None or username
#   POST arg: login
#             register
#     
@app.route('/user/<section>', methods=['POST'])
def user(section):
    global active_user      #to be replaced with cookies
    status = '0'
    _connection = get_flask_database_connection(app)
    user_repository = User_repository(_connection)
    if section == 'login':
        username = request.form['username']
        password = request.form['passcode']
        query_result = user_repository.find(username, password)
        if query_result[0]:
            active_user = copy.copy(query_result[1])
            return redirect('/')
        # --->>> store info in cookies
    elif section == 'register':
        name = request.form['name']
        username = request.form['username']
        password = request.form['passcode']
        query_result = user_repository.add(1, name, username, password)
        if query_result[0]:
            return redirect('/')
    return f"WRONG: {query_result[1]}"






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