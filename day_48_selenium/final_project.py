import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cursor = driver.find_element(By.XPATH, value="//div[@id='buyCursor']")
grandma = driver.find_element(By.XPATH, value="//div[@id='buyGrandma']")
factory = driver.find_element(By.XPATH, value="//div[@id='buyFactory']")
mine = driver.find_element(By.XPATH, value="//div[@id='buyMine']")
shipment = driver.find_element(By.XPATH, value="//div[@id='buyShipment']")
lab = driver.find_element(By.XPATH, value="//div[@id='buyAlchemy lab']")

time_in_5_seconds = time.time() + 5
five_min = time.time() + 60 * 5


def clicking():
    print(f"Clicking was called, biggest is {biggest}")
    print(f"Checking conditions for biggest: {biggest}")
    if biggest >= 100:
        print("Condition 1 met")
        grandma.click()
    elif biggest >= 500:
        print("Condition 2 met")
        factory.click()
    elif biggest >= 2000:
        print("Condition 3 met")
        mine.click()
    elif biggest >= 7000:
        print("Condition 4 met")
        shipment.click()
    else:
        print("I am here")


while True:
    money = int(driver.find_element(By.ID, "money").text)
    driver.find_element(By.XPATH, value="//div[@id='cookie']").click()
    if time.time() > time_in_5_seconds:
        affordable = driver.find_elements(By.XPATH, value="//div[@class='']/b")
        biggest = max([float(item.text.split("-")[1].strip()) for item in affordable])
        print(money)
        if money > biggest:
            clicking()

        time_in_5_seconds += 5

    if time.time() > five_min:
        print(money)
        break

# //div[@class='']
