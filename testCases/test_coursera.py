import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.CourseaLandingPage import CourseraLandingPage

from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_landing:
    baseURL = ReadConfig.getBaseURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_COURSE0001(self, setup):
        self.driver = setup
        CLP = CourseraLandingPage(self.driver)

        self.driver.maximize_window()
        self.driver.get(self.baseURL)


        #Check title
        actual_title = self.driver.title
        if actual_title == "Coursera | Degrees, Certificates, & Free Online Courses":
            self.logger.info("***** Verify Homepage Title : Passed *****")
            assert True
        else:
            self.logger.info("***** Verify Homepage Title : Failed *****")
            assert False

        # Click Login
        CLP.clickLogin()
        time.sleep(3)
        self.logger.info("***** Clicked on Login on Homepage : Passed *****")

        # Click on SSO Login
        CLP.clickSSOLogin()
        self.logger.info("***** Clicked on SSO Google Login: Passed *****")

        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])

        self.logger.info("***** Switched to SSO Window: Passed *****")

        # Fill Email
        CLP.setUserName(self.username)
        self.logger.info("***** Filled Email : Passed *****")
        CLP.clickSSONext()
        time.sleep(3)

        # Fill Password
        CLP.setPassword(self.password)
        self.logger.info("***** Filled Email : Passed *****")
        CLP.clickSSONext()
        time.sleep(3)

        CLP.clickSSOContinue()
        time.sleep(3)

        #Click Submit

