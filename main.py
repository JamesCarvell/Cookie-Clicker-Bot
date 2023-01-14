from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

chrome_driver_path = "C:/Development/chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=Service(chrome_driver_path))

driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(2.0)
lang = driver.find_element(by="id", value="langSelect-EN")
lang.click()

time.sleep(2.0)
cookie = driver.find_element(by="id", value="bigCookie")
helpers = [driver.find_element(by="id", value=f"product{i}") for i in range(18, -1, -1)]

end_time = time.time() + 300.0
print("end time:", {end_time})

for i in range(100):
    cookie.click()
    helpers[-1].click()

while end_time > time.time():
    for i in range(200):
        cookie.click()
    try:
        shop = driver.find_element(by="id", value="upgrade0")
        shop.click()
    except:
        pass
    for helper in helpers:
        try:
            helper.click()
        except:
            pass


print("actual end time:", {time.time()})
cps = driver.find_element(by="id", value="cookiesPerSecond")
print("cps:", {cps.text})

driver.quit()
