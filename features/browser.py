from selenium import webdriver


class Browser:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-dev-shm-usage')
    # driver = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=options)
    driver = webdriver.Chrome(executable_path="C:/chromedriver_win32/chromedriver.exe", options=options)
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(10)
    driver.maximize_window()

    def get_driver(self):
        return self.driver
    # def quit(self):
    #     self.driver.quit()
