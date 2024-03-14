import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get(url="https://secure-retreat-92358.herokuapp.com/")

name = driver.find_element(By.NAME, value="fName")
name.send_keys("Ali")
time.sleep(1)
last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Magomedaliev")
time.sleep(1)
email = driver.find_element(By.NAME, value="email")
email.send_keys("test@test.ru", Keys.ENTER)

time.sleep(3)
























# all_articles = driver.find_element(By.XPATH, value="//a[@title='Special:Statistics']").text
# print(all_articles)
#
# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python", Keys.ENTER)
# time.sleep(2)
