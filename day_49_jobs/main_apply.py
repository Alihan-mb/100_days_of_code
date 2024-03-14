import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", value=True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://makhachkala.superjob.ru/?utm_source=app-registracia-soinskatel-s-rezume&utm_medium=email&utm_campaign=20240109-app-registracia-soinskatel-s-rezume&utm_content=138071929-1-0&curtain%5BreturnUrl%5D=%2F%3Futm_source%3Dapp-registracia-soinskatel-s-rezume%26utm_medium%3Demail%26utm_campaign%3D20240109-app-registracia-soinskatel-s-rezume%26utm_content%3D138071929-1-0&curtain%5BrouteName%5D=authLogin&curtain%5Bid%5D=auth")
wait = WebDriverWait(driver, 10)

login = driver.find_element(By.XPATH, value="//input[@name='login']")
login.send_keys("alihan-mb@list.ru")
password = driver.find_element(By.XPATH, value="//input[@name='password']").send_keys("ZP6942So", Keys.ENTER)

wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='keywords']"))).send_keys("Тестировщик", Keys.ENTER)

driver.find_element(By.XPATH, "//button[@title='Всё верно']").click()
