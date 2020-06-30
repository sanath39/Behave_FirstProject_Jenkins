from .locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.txtbox_username_xpath = Locators.txtbox_username_xpath
        self.txtbox_password_xpath = Locators.txtbox_password_xpath
        self.btn_login_xpath = Locators.btn_login_xpath
        self.span_invalid_info_xpath = Locators.span_invalid_info_xpath

    def setUsername(self, username):
        self.driver.find_element_by_xpath(self.txtbox_username_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.txtbox_password_xpath).send_keys(password)

    def click_login(self):
        return self.driver.find_element_by_xpath(self.btn_login_xpath).click()

    def get_invalid_info(self):
        return self.driver.find_element_by_xpath(self.span_invalid_info_xpath).text
