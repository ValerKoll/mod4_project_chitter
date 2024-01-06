from playwright.sync_api import Page, expect

#
# ref: https://playwright.dev/python/docs/api/class-playwright
# LOCATORS:
# page.get_by_role() to locate by explicit and implicit accessibility attributes.
# page.get_by_text() to locate by text content.
# page.get_by_label() to locate a form control by associated label's text.
# page.get_by_placeholder() to locate an input by placeholder.
# page.get_by_alt_text() to locate an element, usually image, by its text alternative.
# page.get_by_title() to locate an element by its title attribute.
# page.get_by_test_id() to locate an element based on its data-testid attribute (other attributes can be configured).
#
# page.set_content("<div>Foobar</div><div>Bar</div>")
# expect(page.locator("div", has_text="Foo")).to_have_text("Foobar")
#   has_text=re.compile('hElLo "world', re.IGNORECASE)

# ======================
# python -m pytest 'tests/test_app1_route.py' -xvv
# ======================

############################
#   MAIN PAGE
#
#  
"""    GET '/'      """
def test_get_home(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    title = page.locator("h1#title")
    expect(title).to_have_text("Chitter App")

"""  GET '/' list of posts """
def test_get_posts_in_home(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    ul = page.locator("ul#post_list")
    expect(ul).to_contain_text("User:")

"""  GET '/<home_page_section>' current user posts """

############################
#  ACCOUNT PAGE
#
#
"""    GET '/account/<section>'     """
def test_get_account_login(page, test_web_address):
    page.goto(f"http://{test_web_address}/account/login")
    title_tag = page.locator("h1#title")
    expect(title_tag).to_have_text("Please Login")
    
def test_get_account_register(page, test_web_address):
    page.goto(f"http://{test_web_address}/account/register")
    title_tag = page.locator("h1#title")
    expect(title_tag).to_have_text("Register")

def test_get_account_logout(web_client, page, test_web_address):
    response = web_client.post('/user/login', data={'username': 'Peter Pan', 'password': 'peter&1234'})
    #assert response.status_code == 200
    page.goto(f"http://{test_web_address}/account/logout")
    title_tag = page.locator("h1#title")
    expect(title_tag).to_have_text("Chitter App")
    
    
############################
#  USER FUNCTIONS
#
#
"""    GET '/user/<section>'     """
def test_get_user_login(page, test_web_address):
    page.goto(f"http://{test_web_address}/user/login")
    title = page.locator("h1#title")
    expect(title).to_have_text("Home Page")
def test_get_user_register(page, test_web_address):
    page.goto(f"http://{test_web_address}/user/register")
    title = page.locator("h1#title")
    expect(title).to_have_text("Home Page")





############################
"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
#def test_post_count_vowels_eunoia(web_client):
#    response = web_client.post('/login', data={'text': 'eunoia'})
#    assert response.status_code == 200
#    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'
