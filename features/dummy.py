from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:/chromedriver_win32/chromedriver.exe")
driver.set_page_load_timeout(30)
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")
driver.find_element_by_xpath("//input[@id='txtUsername']").send_keys("Admin")
driver.find_element_by_xpath("//input[@id='txtPassword']").send_keys("admin123")
driver.find_element_by_xpath("//input[@id='btnLogin']").click()

driver.find_element_by_xpath("//b[contains(text(),'Leave')]").click()
driver.find_element_by_xpath("//a[@id='menu_leave_assignLeave']").click()
import time
time.sleep(5)
# driver.find_element_by_xpath("//a[@id='menu_leave_assignLeave']").clear()
driver.find_element_by_xpath("//input[@id='assignleave_txtEmployee_empName']").send_keys("Linda Anderson")
leave = Select(driver.find_element_by_xpath("//select[@id='assignleave_txtLeaveType']"))
leave.select_by_visible_text("Vacation US")
driver.find_element_by_xpath("//input[@id='assignleave_txtFromDate']").clear()
driver.find_element_by_xpath("//input[@id='assignleave_txtFromDate']").send_keys("01-05-2020")
driver.find_element_by_xpath("//input[@id='assignleave_txtToDate']").clear()
driver.find_element_by_xpath("//input[@id='assignleave_txtToDate']").send_keys("02-05-2020")
part_day = Select(driver.find_element_by_xpath("//select[@id='assignleave_partialDays']"))
part_day.select_by_visible_text("None")
driver.find_element_by_xpath("//textarea[@id='assignleave_txtComment']").send_keys("..............")
driver.find_element_by_xpath("//input[@id='assignBtn']").click()
time.sleep(3)
driver.find_element_by_xpath("//input[@id='confirmOkButton']").click()
time.sleep(7)
driver.close()
driver.quit()
