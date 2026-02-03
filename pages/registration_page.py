from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        self.username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        self.password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        self.registration_button = page.get_by_test_id('registration-page-registration-button')

    def fill_email_input(self, email: str):
        expect(self.email_input).to_be_visible()
        self.email_input.fill(email)
        expect(self.email_input).to_have_value(email)

    def fill_username_input(self, username: str):
        expect(self.username_input).to_be_visible()
        self.username_input.fill(username)
        expect(self.username_input).to_have_value(username)

    def fill_password_input(self, password: str):
        expect(self.password_input).to_be_visible()
        self.password_input.fill(password)
        expect(self.password_input).to_have_value(password)

    def click_registration_button(self):
        expect(self.registration_button).to_be_visible()
        expect(self.registration_button).not_to_be_disabled()
        self.registration_button.click()