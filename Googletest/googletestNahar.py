
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Launch Browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Go to Home Page
driver.get("https://www.google.com/")
time.sleep(3)

# Step 3: Go to Search Button
Search = driver.find_element(By.NAME, "q")
Search.send_keys("Bangladesh RMG")
time.sleep(2)

# Step 4: Click Search Button
search_button = driver.find_element(By.NAME, "btnK")
search_button.click()
time.sleep(5)

