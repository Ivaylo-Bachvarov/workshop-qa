from playwright.sync_api import Page


class LoginPage:
    def __init__(self) -> None:
        self.url = 'https://automation-workshop.hacksoft.io/admin/'

    def goto(self, page):
        page.goto(self.url)

    def username_field(self, page: Page):
        return page.locator('#id_username')

    def password_field(self, page: Page):
        return page.locator('#id_password')

    def submit_button(self, page: Page):
        return page.locator('//*[@id="login-form"]/div[3]/input')
