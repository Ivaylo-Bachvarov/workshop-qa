from playwright.sync_api import expect
from pages import AdminPage, LoginPage
import os
from dotenv import load_dotenv
load_dotenv()


def login_flow(page, username, password):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.username_field().fill(username)
    login_page.password_field().fill(password)
    login_page.submit_button().click()

    return page


def test_login_with_proper_credentials(page):
    login_flow(page, os.getenv('USERNAME'), os.getenv('PASSWORD'))

    admin_page = AdminPage(page)
    expect(page).to_have_url(admin_page.url)


def test_login_with_wrong_credentials(page):
    login_flow(page, 'wrong_username', 'wrong_password')

    error_message_element = page.locator('.errornote')
    expect(error_message_element).to_be_visible()
