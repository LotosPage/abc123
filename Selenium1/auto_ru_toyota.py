from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import *

driver=webdriver.Chrome("D:\\chromedriver.exe")
driver.set_page_load_timeout(60)
driver.get("http://www.auto.ru")
driver.maximize_window()
driver.implicitly_wait(30)
driver.get_screenshot_as_file("C:\\Users\\Admin\\PycharmProjects\\abc123\Selenium1\\screenshots\\Auto_ru_toyota1.png")
driver.find_element_by_xpath('//*[@id=\"confirm-button\"]').click()
sleep (5)
driver.get_screenshot_as_file("C:\\Users\\Admin\\PycharmProjects\\abc123\Selenium1\\screenshots\\Auto_ru_toyota2.png")
toyota = driver.find_element_by_xpath('//*[@id="LayoutIndex"]/div/div/div[1]/div[2]/div[1]/div[2]/div/div[6]/a[2]/div[1]')
toyota.click()
# driver.find_elements_by_css_selector('#listing-filters > div.ListingCarsFilters-module__container > div.ListingCarsFilters-module__mainForm > div:nth-child(1) > div > div > div.MMMMultiFilter-module__MMMMultiFilter__item > div > div:nth-child(2) > div > input[type="hidden"]')
# driver.find_element_by_xpath('#listing-filters > div.ListingCarsFilters-module__container > div.ListingCarsFilters-module__mainForm > div:nth-child(1) > div > div > div.MMMMultiFilter-module__MMMMultiFilter__item > div > div:nth-child(2) > div > input[type="hidden"]')
# driver.find_element_by_css_selector('#listing-filters > div.ListingCarsFilters-module__container > div.ListingCarsFilters-module__mainForm > div:nth-child(1) > div > div > div.MMMMultiFilter-module__MMMMultiFilter__item > div > div:nth-child(2) > div > input[type="hidden"]')
driver.find_element_by_xpath('')
# driver.find_element_by_xpath('//*[@id="listing-filters"]/div[2]/div[2]/div[1]/div/div/div[1]/div/div[2]/div/input').send_keys("toyota")
driver.get_screenshot_as_file("C:\\Users\\Admin\\PycharmProjects\\abc123\Selenium1\\screenshots\\Auto_ru_toyota3.png")
driver.quit()
