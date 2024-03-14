import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

time_list = driver.find_elements(By.XPATH, value='//div[@class="medium-widget event-widget last"]//ul//li//time')
theme_list = driver.find_elements(By.XPATH, value='//div[@class="medium-widget event-widget last"]//ul//li//a')

events = {}

for i in range(len(time_list)):
    events[i] = {
        "time":time_list[i].text,
        "name":theme_list[i].text
    }



























for n in range(len(theme_list)):
    events[n] = {
        "time": time_list[n].text,
        "name": theme_list[n].text
    }
print(events)




driver.quit()