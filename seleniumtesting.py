import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\chrome driver\chromedriver.exe")

driver.get("https://www.saucedemo.com/")

driver.maximize_window()

usr_ele =driver.find_element_by_name("user-name")
usr_ele.send_keys("standard_user")

pwd_ele=driver.find_element_by_name("password")
pwd_ele.send_keys("secret_sauce")

driver.find_element_by_id("login-button").click()

time.sleep(3)
driver.find_element_by_xpath("//button[contains(@class,'btn_primary btn_inventory')]").click()
driver.find_element_by_xpath("//button[contains(@class,'btn_primary btn_inventory')]").click()
driver.find_element_by_xpath("//button[contains(@class,'btn_primary btn_inventory')]").click()

time.sleep(3)
driver.find_element_by_id("shopping_cart_container").click()

time.sleep(3)
driver.find_element_by_xpath("//a[contains(text(),'CHECKOUT')]").click()

time.sleep(3)
fst_name=driver.find_element_by_id("first-name")
fst_name.send_keys("User")

time.sleep(3)
lst_name=driver.find_element_by_id("last-name")
lst_name.send_keys("khan")


time.sleep(3)
zip=driver.find_element_by_id("postal-code")
zip.send_keys("421302")


time.sleep(3)
driver.find_element_by_xpath("//input[@class='btn_primary cart_button']").click()

time.sleep(3)
driver.find_element_by_xpath("//a[@class='btn_action cart_button']").click()

time.sleep(2)
driver.close()
