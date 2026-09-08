import allure  # Импортируем allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.input import Input


class LoginFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, locator='login-form-email-input', name='Email')
        self.password_input = Input(page, locator='login-form-password-input', name='Password')

    @allure.step("Fill login form")  # Добавили allure шаг
    def fill(self, email: str, password: str):
        self.email_input.fill(email)
        self.password_input.fill(password)

    @allure.step("Check visible login form")  # Добавили allure шаг
    def check_visible(self, email: str, password: str):
        self.email_input.check_visible()
        self.password_input.check_visible()

        if email:
            self.email_input.check_have_text(email)
        if password:
            self.password_input.check_have_text(password)
