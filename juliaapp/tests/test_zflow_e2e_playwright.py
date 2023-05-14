from playwright.sync_api import Page, expect
import re
from juliaapp.models import User
# pytest -v --slowmo 1000  --headed   
# run app in a seperate terminal to allow it to interface with the browser

import string
import random
res = ''.join(random.choices(string.ascii_letters, k=32))
hex_val = str(''.join(random.choices(string.hexdigits, k=6))).upper()

def test_signup_flow_e2e(page: Page):
    # TODO: GIVE PLAYWRIGHT TESTS LOCAL LAUNCH/DB etc.
    page.goto("http://127.0.0.1:8000")
    expect(page).to_have_title(re.compile("Landing"))
    body = page.locator("body")
    expect(body).to_have_text(re.compile(".*PLEASE DO NOT SUBMIT ANY PERSONAL DATA TO THIS WEBSITE, IT IS PURELY A TECHNICAL EXPERIMENT!.*"))
    login = page.get_by_role("link", name="Login")
    login.click()
    signup = page.get_by_role("link", name="Signup Here")
    signup.click()
    page.get_by_placeholder("Username").fill(str(res))
    page.get_by_placeholder("Email").fill(f"{str(res)}@gmail.com")
    page.get_by_placeholder("Password", exact=True).fill(str(res))
    page.get_by_placeholder("Confirm Password").fill(str(res))
    page.get_by_role("button", name="Signup").click()
    expect(page).to_have_url(re.compile(f".*profile/{str(res)}.*"))

def test_logout_flow_e2e(page: Page):
    page.goto("http://127.0.0.1:8000")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Email").fill("silas@gmail.com")
    page.get_by_placeholder("Password").fill("password")
    page.get_by_placeholder("Password").press("Enter")
    page.get_by_role("link", name="Logout").click()
    text_on_footer = page.eval_on_selector("footer", "e => e.textContent")
    assert "Logout" not in text_on_footer

def test_generate_flow_e2e(page: Page):
    page.goto("http://127.0.0.1:8000")
    page.get_by_role("link", name="Login").click()
    page.get_by_placeholder("Email").fill("silas@gmail.com")
    page.get_by_placeholder("Password").fill("password")
    page.get_by_placeholder("Password").press("Enter")
    page.get_by_role("link", name="Generate").click()
    page.get_by_placeholder("Hex value (RRGGBB)").fill(str(hex_val))
    page.get_by_role("button", name="Generate").click()
    img_element = page.query_selector(f'img[src="/mandelbrot/{str(hex_val)}"][alt="Coloured picture of mandelbrot"]')
    assert img_element is not None

