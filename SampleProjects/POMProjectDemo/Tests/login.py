
from selenium import webdriver
import time
import unittest
from SampleProjects.POMProjectDemo.Pages.loginPage import LoginPage
from SampleProjects.POMProjectDemo.Pages.homePage import HomePage
from selenium.webdriver.common.by import By

class LoginTest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="c:\selenium-browser-driver\chromedriver")
        # cls.driver.implicity_wait(10)
        cls.driver.maximize_window()


    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        time.sleep(2)
        login.enter_username("Admin")
        time.sleep(2)
        login.enter_password("admin123")
        time.sleep(2)
        login.click_login()

        time.sleep(2)

        homepage = HomePage(driver)
        time.sleep(2)
        homepage.click_welcome()
        time.sleep(2)
        homepage.click_logout()


        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        # cls.print("Test completed")

    if __name__  == '_main_':
      unittest.main()
