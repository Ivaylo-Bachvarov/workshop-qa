from playwright.sync_api import Page
from pages import LoginPage

import os


def login_flow(page, username, password):
    login_page = LoginPage()
    login_page.goto(page)
    login_page.username_field(page).fill(username)
    login_page.password_field(page).fill(password)
    login_page.submit_button(page).click()

    return page


def test_login_with_proper_credentials(page: Page):
    page = login_flow(page, os.environ['USERNAME'], os.environ['PASSWORD'])
    page.goto('https://automation-workshop.hacksoft.io/admin/reservations/property/')
    print(page.locator('.field-address').count())
