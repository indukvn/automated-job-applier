from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# both email and password must be registered in linkedIn
email = "your mail address"
password = "your password "
PHONE = "your number"

job_link = "https://www.linkedin.com/jobs/search/?currentJobId=3289320701&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom"

chrome_driver_path = "/Users/Indu/OneDrive/Desktop/development/chromedriver"
driver = Chrome(chrome_driver_path)
driver.get(job_link)

sign_in_button = driver.find_element(By.LINK_TEXT, "Sign in")
sign_in_button.click()

time.sleep(5)

email_field = driver.find_element(By.ID, "username")
email_field.send_keys(email)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)

time.sleep(5)
apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
apply_button.click()

time.sleep(5)
phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
if phone.text == "":
    phone.send_keys(PHONE)

submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
submit_button.click()