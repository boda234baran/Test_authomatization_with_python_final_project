from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import MainPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_url.click()
        assert ('login' in browser.current_url),\
            'No "Login" word in URL'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),\
            "The registration form is not presented at login and registration link"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRARION_FORM),\
            "The registration form is not presented at login and registration link"
