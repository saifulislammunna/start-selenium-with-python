
from selenium import webdriver
import time
import unittest
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="c:\selenium-browser-driver\chromedriver")
        # cls.driver.implicity_wait(10)
        cls.driver.maximize_window()


    def test_login_valid(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='txtUsername']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='txtUsername']").send_keys("Admin")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='txtPassword']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='txtPassword']").send_keys("admin123")
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//*[@id='btnLogin']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='welcome']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='welcome-menu']/ul/li[3]/a").click()
        time.sleep(2)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        cls.print("Test completed")

    if __name__  == '_main_':
      unittest.main()