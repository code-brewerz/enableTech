from selenium.webdriver.common.by import By

class SauceDemoPage:

    textbox_username_xpath = "//input[@id = 'user-name']"
    textbox_password_xpath = "//input[@id = 'password']"
    login_btn_xpath = "//input[@id='login-button']"

    def __init__(self, driver):
        self.driver = driver

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_btn_xpath).click()

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)