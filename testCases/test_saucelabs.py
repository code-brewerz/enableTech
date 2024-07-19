import random
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import initialize_creds
from pageObjects.SauceDemoPage import SauceDemoPage
from pageObjects.SauceInvPage import SauceInvPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_landing:
    baseURL = ReadConfig.getSauceURL()
    fname, lname, zipcode = initialize_creds()
    logger = LogGen.loggen()

    @pytest.mark.parametrize("username,password", [
        ("standard_user", "secret_sauce"),
        ("locked_out_user", "secret_sauce"),
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
    ])
    def test_SAUCELABS(self, setup, username, password):
        self.driver = setup
        SDP = SauceDemoPage(self.driver)
        SIP = SauceInvPage(self.driver)

        self.driver.maximize_window()
        self.driver.get(self.baseURL)

        # Check title
        actual_title = self.driver.title
        if actual_title == "Swag Labs":
            self.logger.info("***** Verify Homepage Title : Passed *****")
            assert True
        else:
            self.logger.info("***** Verify Homepage Title : Failed *****")
            assert False

        SDP.setUserName(username)
        SDP.setPassword(password)
        time.sleep(5)

        SDP.clickLogin()

        # Check for Products Page

        if self.driver.find_element(By.XPATH, "//div[@class='inventory_list']").is_displayed():
            self.logger.info("***** Login Successful : Passed *****")
            self.driver.save_screenshot(".\\Screenshots\\" + f"{self.test_SAUCELABS.__name__}_{username}_Login_Pass.png")
            assert True

        else:

            self.logger.info("***** Login Successful  : Failed *****")
            self.driver.save_screenshot(".\\Screenshots\\" + f"{self.test_SAUCELABS.__name__}_{username}_Login_Fail.png")
            assert False

        # Add random products to cart from list

        inv_items = self.driver.find_elements(By.XPATH, SIP.inv_items_xpath)

        for i in range(0, 2):
            random_index = random.randint(1, len(inv_items))
            SIP.clickAddCartByIndex(random_index)
            time.sleep(2)

        actual_badge_counter = self.driver.find_element(By.XPATH, SIP.badge_counter_xpath).text


        # Click On Cart Badge
        SIP.clickOnCartInv()

        cart_items = self.driver.find_elements(By.XPATH, SIP.cart_items_xpath)

        if actual_badge_counter == str(len(cart_items)):
            self.logger.info("***** Two Products Added : Passed *****")
            self.driver.save_screenshot(".\\Screenshots\\" + f"{self.test_SAUCELABS.__name__}_{username}_Add_Products_Pass.png")
            assert True

        else:
            self.logger.info("***** Two Products Added : Failed *****")
            self.driver.save_screenshot(".\\Screenshots\\" + f"{self.test_SAUCELABS.__name__}_{username}_Add_Products_Fail.png")
            assert False


        SIP.clickOnCheckout()

        # Check Checkout Info Page displayed
        if self.driver.find_element(By.XPATH, "//div[contains(@class,'checkout_info_container')]").is_displayed():
            assert True
            self.logger.info("***** Checkout Page Visible : Passed *****")
        else:
            assert False
            self.logger.info("***** Checkout Page Visible : Failed *****")

        SIP.setFname(self.fname)
        SIP.setLname(self.lname)
        SIP.setZipcode(self.zipcode)
        time.sleep(2)
        # Click on Checkout on Continue
        SIP.clickOnCheckoutContinue()

        # Check Checkout Overview Page displayed
        if self.driver.find_element(By.XPATH, "//div[contains(@class,'checkout_summary_container')]").is_displayed():
            self.logger.info("***** Checkout Summary Page Visible : Passed *****")
            assert True
        else:
            self.logger.info("***** Checkout Summary Page Visible : Failed *****")
            assert False

        cart_item_prices = self.driver.find_elements(By.XPATH, SIP.cart_item_prices)

        actual_total = 0.00
        for cart_item in cart_item_prices:
            price = float(cart_item.text.replace('$', ''))
            actual_total += price

        actual_tax = round(actual_total * 0.08, 2)
        actual_final = round(actual_total + actual_tax, 2)

        cart_total = (self.driver.find_element(By.XPATH, SIP.cart_total_xpath).text).split(": $")[1]
        cart_tax = (self.driver.find_element(By.XPATH, SIP.cart_tax_xpath).text).split(": $")[1]
        cart_final = (self.driver.find_element(By.XPATH, SIP.cart_final_total).text).split(": $")[1]

        # self.logger.info(actual_total)
        # self.logger.info(cart_total)
        # self.logger.info(actual_tax)
        # self.logger.info(cart_tax)
        # self.logger.info(actual_final)
        # self.logger.info(cart_final)

        if (actual_total == round(float(cart_total), 2) and actual_tax == round(float(cart_tax), 2) and actual_final == round(float(cart_final), 2)):
            self.logger.info("***** Checkout Summary Matched : Passed *****")
            self.driver.save_screenshot(".\\Screenshots\\" + f"{self.test_SAUCELABS.__name__}_{username}_Checkout_Pass.png")
            assert True
        else:

            self.logger.info("***** Checkout Summary Matched : Failed *****")
            self.driver.save_screenshot(".\\Screenshots\\" + f"{self.test_SAUCELABS.__name__}_{username}_Checkout_Fail.png")
            assert False

        SIP.clickOnFinishCheckout()

        # Check Checkout Overview Page displayed
        if self.driver.find_element(By.XPATH, "//div[@class='checkout_complete_container']").is_displayed():
            self.driver.save_screenshot(".\\Screenshots\\" + f"{self.test_SAUCELABS.__name__}_{username}_Order_Pass.png")
            self.logger.info("***** Order Placed : Passed *****")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + f"{self.test_SAUCELABS.__name__}_{username}_Order_Fail.png")
            self.logger.info("***** Order Placed: Failed *****")
            assert False

        self.driver.quit()