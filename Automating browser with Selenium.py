# 16. Automating browser with Selenium
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://google.com")
print(driver.title)
driver.quit()
