import os

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# Get linkedIn login information
email_address = os.environ.get("email", "Couldn't find email address")
password = os.environ.get("password", "Couldn't find password")

# Instantiate options
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

# Instantiate driver
driver = webdriver.Chrome(options=options)

# Open browser to the linked in
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

# Sign in with email and password
sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

email_textfield = driver.find_element(By.ID, "username")
email_textfield.send_keys(email_address)

password_textfield = driver.find_element(By.ID, "password")
password_textfield.send_keys(password)

sign_in_button = driver.find_element(By.CLASS_NAME, "login__form_action_container ")
sign_in_button.click()





