from selenium.webdriver.common.by import By

class SauceInvPage:

    inv_items_xpath = "//div[@class='inventory_list']/div[@class='inventory_item']"
    badge_counter_xpath = "//a//span[contains(@class,'shopping_cart_badge')]"
    cart_items_xpath = "//div[@class='cart_list']//div[@class='cart_item']"
    checkout_btn_xpath = "//a[contains(@class,'checkout_button')]"

    #Checkout info
    fname_xpath = "//input[@id='first-name']"
    lname_xpath = "//input[@id='last-name']"
    zipcode_xpath = "//input[@id='postal-code']"
    checkout_continue_xpath = "//input[contains(@value,'CONTINUE')]"

    # Checkout Summary
    cart_item_prices = "//div[@class='cart_item']//div[@class='inventory_item_price']"
    cart_total_xpath = "//div[contains(@class,'summary_subtotal_label')]"
    cart_tax_xpath = "//div[contains(@class,'summary_tax_label')]"
    cart_final_total = "//div[contains(@class,'summary_total_label')]"
    cart_finish_button = "//a[contains(text(), 'FINISH')]"


    def __init__(self, driver):
        self.driver = driver

    def clickAddCartByIndex(self, index):
        self.driver.find_element(By.XPATH, self.inv_items_xpath + "[" + str(index) + "]" + "//button").click()

    def clickOnCartInv(self):
        self.driver.find_element(By.XPATH, self.badge_counter_xpath).click()

    def clickOnCheckout(self):
        self.driver.find_element(By.XPATH, self.checkout_btn_xpath).click()

    # Checkout info

    def setFname(self, username):
        self.driver.find_element(By.XPATH, self.fname_xpath).clear()
        self.driver.find_element(By.XPATH, self.fname_xpath).send_keys(username)

    def setLname(self, password):
        self.driver.find_element(By.XPATH, self.lname_xpath).clear()
        self.driver.find_element(By.XPATH, self.lname_xpath).send_keys(password)

    def setZipcode(self, username):
        self.driver.find_element(By.XPATH, self.zipcode_xpath).clear()
        self.driver.find_element(By.XPATH, self.zipcode_xpath).send_keys(username)

    def clickOnCheckoutContinue(self):
        self.driver.find_element(By.XPATH, self.checkout_continue_xpath).click()

    def clickOnFinishCheckout(self):
        self.driver.find_element(By.XPATH, self.cart_finish_button).click()

    # Checkout Summary