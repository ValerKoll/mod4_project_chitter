#assert web_client.arg['...']==    #arg =/pageurl?...=1
#assert response.data.decode("utf-8") == ""

############################
#   ROUTE TESTS
#
#  
"""    GET '/'      """
def test_get_home(web_client, page):
    response = web_client.get('/')
    assert response.status_code == 200

"""    GET '/account/<section>'     """
def test_get_account_login(web_client, page):
    response = web_client.get('/account/login')
    assert response.status_code == 200

"""    GET '/user/<section>'     """
def test_get_user_login(web_client, page):
    response = web_client.post('/user/login')
    assert response.status_code == 200