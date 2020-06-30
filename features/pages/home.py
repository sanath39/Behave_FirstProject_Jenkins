from .locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver

        self.btn_welcome = Locators.btn_welcome_xpath
        self.btn_logout = Locators.btn_logout_xpath
        self.span_assign_leave = Locators.span_assign_leave_xpath
        self.span_leave = Locators.span_leave_xpath
        self.span_quick_assign_leave = Locators.span_quick_assign_leave_xpath

    def click_welcome(self):
        return self.driver.find_element_by_xpath(self.btn_welcome).click()

    def click_logout(self):
        return self.driver.find_element_by_xpath(self.btn_logout).click()

    def click_leave(self):
        return self.driver.find_element_by_xpath(self.span_leave).click()

    def click_assign_leave(self):
        return self.driver.find_element_by_xpath(self.span_assign_leave).click()

    def click_quick_assign_leave(self):
        return self.driver.find_element_by_xpath(self.span_quick_assign_leave).click()
