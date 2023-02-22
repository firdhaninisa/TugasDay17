import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_a_success_login(self):
        #step
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") #buka situs        
        driver.find_element(By.ID,"user-name").send_keys("standard_user") #isi email
        driver.find_element(By.ID,"password").send_keys("secret_sauce") #isi password
        driver.find_element(By.ID, "login-button").click()

    #validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('PRODUCT', response_data)

    def test_b_failed_login_blank_password(self):
        #step
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") #buka situs        
        driver.find_element(By.ID,"user-name").send_keys("standard_user") #isi email
        driver.find_element(By.ID, "login-button").click()
 
    #validasi
        response_data = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3").text
        self.assertEqual(response_data, "Epic sadface: Password is required")

    def test_c_add_to_cart(self):
        #step
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") #buka situs        
        driver.find_element(By.ID,"user-name").send_keys("standard_user") #isi email
        driver.find_element(By.ID,"password").send_keys("secret_sauce") #isi password
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
 
    #validasi
        response_data = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
        self.assertEqual('1', response_data)

    def test_d_see_product(self):
        #step
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") #buka situs        
        driver.find_element(By.ID,"user-name").send_keys("standard_user") #isi email
        driver.find_element(By.ID,"password").send_keys("secret_sauce") #isi password
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.ID, "item_4_title_link").click()
 
    #validasi
        response_data = driver.find_element(By.XPATH,"//*[@id='back-to-products']").text
        self.assertEqual('BACK TO PRODUCTS', response_data)

    def test_d_remove_from_cart(self):
        #step
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") #buka situs        
        driver.find_element(By.ID,"user-name").send_keys("standard_user") #isi email
        driver.find_element(By.ID,"password").send_keys("secret_sauce") #isi password
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
 
    #validasi
        response_data = driver.find_element(By.XPATH,"//*[@id='add-to-cart-sauce-labs-backpack']").text
        self.assertEqual('ADD TO CART', response_data)            

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()        