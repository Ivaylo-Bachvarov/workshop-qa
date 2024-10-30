from constants import BASE_URL


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = BASE_URL + '/admin/login/'

    def goto(self):
        self.page.goto(self.url)

    def username_field(self):
        return self.page.locator('#id_username')

    def password_field(self):
        return self.page.locator('#id_password')

    def submit_button(self):
        return self.page.locator('//*[@id="login-form"]/div[3]/input')


class AdminPage:
    def __init__(self, page):
        self.page = page
        self.url = BASE_URL + '/admin/'

    def goto(self):
        self.page.goto(self.url)
