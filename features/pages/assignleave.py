from .locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class LeavePage:

    def __init__(self, driver):
        self.driver = driver

        self.txt_emp_name_xpath = Locators.txt_emp_name_xpath
        self.ddl_leave_type_xpath = Locators.ddl_leave_type_xpath
        self.date_pick_from_date_xpath = Locators.date_pick_from_date_xpath
        self.date_pick_to_date_xpath = Locators.date_pick_to_date_xpath
        self.ddl_part_days_xpath = Locators.ddl_part_days_xpath
        self.txt_area_comment_xpath = Locators.txt_area_comment_xpath
        self.btn_assign_xpath = Locators.btn_assign_xpath
        self.btn_confirm_ok_xpath = Locators.btn_confirm_ok_xpath

    def set_emp_name(self, name):
        self.driver.find_element_by_xpath(self.txt_emp_name_xpath).clear()
        return self.driver.find_element_by_xpath(self.txt_emp_name_xpath).send_keys(name)

    def get_leave_type(self):
        return self.driver.find_element_by_xpath(self.ddl_leave_type_xpath)

    def set_from_date(self, from_date):
        self.driver.find_element_by_xpath(self.date_pick_from_date_xpath).clear()
        return self.driver.find_element_by_xpath(self.date_pick_from_date_xpath).send_keys(from_date)

    def set_to_date(self, to_date):
        self.driver.find_element_by_xpath(self.date_pick_to_date_xpath).clear()
        return self.driver.find_element_by_xpath(self.date_pick_to_date_xpath).send_keys(to_date)

    def get_partial_days(self):
        return self.driver.find_element_by_xpath(self.ddl_part_days_xpath)

    def set_comment(self, comment):
        self.driver.find_element_by_xpath(self.txt_area_comment_xpath).clear()
        return self.driver.find_element_by_xpath(self.txt_area_comment_xpath).send_keys(comment)

    def click_assign(self):
        return self.driver.find_element_by_xpath(self.btn_assign_xpath).click()

    def click_ok_confirm(self):
        return self.driver.find_element_by_xpath(self.btn_confirm_ok_xpath).click()