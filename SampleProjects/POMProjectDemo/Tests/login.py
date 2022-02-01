from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="c:\selenium-browser-driver\chromedriver")

# driver.implicity_wait(10)
# driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='txtUsername']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='txtUsername']").send_keys("Admin")
time.sleep(5)
driver.find_element(By.XPATH, "//*[@id='txtPassword']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='txtPassword']").send_keys("admin123")
time.sleep(5)

driver.find_element(By.XPATH, "//*[@id='btnLogin']").click()

driver.close()
driver.quit()
print("Test completed")