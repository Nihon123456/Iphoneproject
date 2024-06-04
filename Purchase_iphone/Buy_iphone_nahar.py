import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Step 1: Launch Browser
driver = webdriver.Firefox()
driver.maximize_window()

# Step 2: Go to Home Page
driver.get("https://tutorialsninja.com/demo/")
time.sleep(3)

# Step 3: Go to Registration page from My Account
my_account = driver.find_element(By.CSS_SELECTOR, ".list-inline .dropdown .hidden-md")
my_account.click()
time.sleep(2)

login = driver.find_element(By.CSS_SELECTOR, ".list-inline  ul > li:nth-of-type(2) > a")
login.click()
time.sleep(2)

# Step 4: Login page
email = driver.find_element(By.CSS_SELECTOR, "input#input-email")
email.send_keys("mail123@gmail.com")
time.sleep(2)

password = driver.find_element(By.CSS_SELECTOR,"#input-password")
password.send_keys("123456")
time.sleep(2)

login_button = driver.find_element(By.CSS_SELECTOR, "[action] .btn-primary")
login_button.click()
time.sleep(5)

home_page_link = driver.find_element(By.LINK_TEXT, "Qafox.com")
home_page_link.click()
time.sleep(2)

iphone = driver.find_element(By.CSS_SELECTOR, ".row > div:nth-of-type(2) h4 > a")
iphone.click()
time.sleep(2)

# iphone details page
add_to_cart = driver.find_element(By.CSS_SELECTOR, "button#button-cart")
add_to_cart.click()
time.sleep(2)

# verify success message for item add to cart
expected_success_text = """Success: You have added iPhone to your shopping cart!
×"""

actual_success_element = driver.find_element(By.CLASS_NAME, 'alert-success')
actual_success_text = actual_success_element.text


if expected_success_text == actual_success_text:
    print("Item added successfully.Test Passed")
else:
    print("Item add failed.Test Failed")

checkout = driver.find_element(By.CSS_SELECTOR, "a[title='Checkout'] > .hidden-md.hidden-sm.hidden-xs")
checkout.click()
time.sleep(2)

final_checkout = driver.find_element(By.CSS_SELECTOR, "#content div:nth-child(8) .btn-primary")
final_checkout.click()
time.sleep(2)