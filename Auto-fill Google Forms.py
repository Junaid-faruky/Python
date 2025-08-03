from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://forms.gle/your-form-url")

# example: fill a text input (adjust selectors per form)
element = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
element.send_keys("Test response")
submit = driver.find_element(By.CSS_SELECTOR, "div[role='button']")
submit.click()
