import time
from msilib.schema import CheckBox
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver import webdriver = "chromedriver.exe"
#driver = Chrome(webdriver)
#driver.get(url)
#time.sleep(5)
#s = driver.find_element_by_css_selector("div.c2h3.c2h9.c2e7").text

browser =webdriver.Chrome("d:\GitHub\Advance-Py\chromedriver.exe")
browser.maximize_window()
browser.get("http://live.skillbox.ru")
daniil_pilipenko= '//*[@id="#app"]/main/div/div/div[2]/div[1]/div[2]/ul/li[1]/label/span'

checkBox = browser.find_element(by=By.XPATH, value=daniil_pilipenko)
checkBox.click()
time.sleep(5)
webinars = browser.find_elements(by=By.CSS_SELECTOR, value='.webinar-card__title')
for webinar in webinars:
    print(webinar.text)