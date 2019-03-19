from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome("D:\\chromedriver.exe")
driver.set_page_load_timeout(60)
driver.get("http://www.kolesa.kz")
driver.maximize_window()
driver.implicitly_wait(30)
driver.get_screenshot_as_file("C:\\Users\\Admin\\PycharmProjects\\abc123\Selenium1\\screenshots\\Kolesa0.png")
zapchasti = driver.find_elements_by_xpath('/html/body/header/nav/div[2]/ul/li[2]/a')
if len(zapchasti) > 0:
    zapchasti[0].click()
# driver.implicitly_wait(10)
shiny = driver.find_elements_by(e)
shiny.click()
# print(shiny[0].text)



driver.quit()
