from selenium.webdriver.common.by import By


class CourseraLandingPage:
    login_button_xpath = "//a[contains(@href, 'login')]"
    sso_google_button_xpath = "//button[contains(@data-track-component, 'google')]"
    sso_next_button_xpath = "//button//span[contains(text(),'Next')]"
    sso_continue_button_xpath = "//button//span[contains(text(),'Continue')]"
    textbox_username_xpath = "//input[@type='email']"
    textbox_password_xpath = "//input[@type='password']"

    def __init__(self, driver):
        self.driver = driver

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def clickSSOLogin(self):
        self.driver.find_element(By.XPATH, self.sso_google_button_xpath).click()

    def clickSSONext(self):
        self.driver.find_element(By.XPATH, self.sso_next_button_xpath).click()

    def clickSSOContinue(self):
        self.driver.find_element(By.XPATH, self.sso_continue_button_xpath).click()

    def setUserName(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)
