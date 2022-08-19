from sys import path_importer_cache
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

# Github credentials
username = "kop_robo"
password = "InstaTest2!"
path_to_photos = "path"

def drag_and_drop_file(drop_target, path):
    driver = drop_target.parent
    file_input = driver.execute_script(JS_DROP_FILE, drop_target, 0, 0)
    file_input.send_keys(path)

# initialize the Chrome driver
driver = webdriver.Chrome("C:\webdrivers\chromedriver")
# head to github login page
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
driver.implicitly_wait(10)
driver.find_element_by_xpath("//button[text()='Zezwól tylko na niezbędne pliki cookie']").click()
driver.find_element_by_name("username").send_keys(username)
driver.find_element_by_name("password").send_keys(password) 
driver.find_element_by_xpath("// div[contains(text(),\'Zaloguj się')]").click()
driver.find_element_by_xpath("//button[text()='Nie teraz']").click()
driver.find_element_by_class_name("_acub").click()
dragdrop = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div')
dragdrop.send_keys(path_to_photos)