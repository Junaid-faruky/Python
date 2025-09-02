from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.python.org")
driver.save_screenshot("python.png")
driver.quit()
