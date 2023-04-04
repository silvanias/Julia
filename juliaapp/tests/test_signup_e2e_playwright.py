from playwright.sync_api import Page, expect
import re
# Mocking, how to do it (postgres vs sqlite)
# pytest -v --slowmo 1000  --headed   

'''
def test_signup_flow(page: Page):
    # TODO: GIVE PLAYWRIGHT TESTS LOCAL LAUNCH/DB etc.
    page.goto("http://127.0.0.1:5001")
    expect(page).to_have_title(re.compile("Landing"))

    body = page.locator("body")
    expect(body).to_have_text(re.compile(".*PLEASE DO NOT SUBMIT ANY PERSONAL DATA TO THIS WEBSITE, IT IS PURELY A TECHNICAL EXPERIMENT!.*"))

    login = page.get_by_role("link", name="Login")
    login.click()

    signup = page.get_by_role("link", name="Signup Here")
    signup.click()

    page.get_by_placeholder("Username").fill("incertus")
    page.get_by_placeholder("Email").fill("incertus@gmail.com")
    page.get_by_placeholder("Password", exact=True).fill("password12345")
    page.get_by_placeholder("Confirm Password").fill("password12345")

    page.get_by_role("button", name="Signup").click()
    expect(page).to_have_url(re.compile(".*incertus"))    '''