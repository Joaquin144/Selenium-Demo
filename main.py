# We are using it to set PATH variable to SeleniumDrivers as we don't want to have them defined globally on our machine
import os
# webdriver emulates a browser for us
from selenium import webdriver

# r prefix means robust string. We use it before path value
# os.environ['PATH'] += r"C:/SSD Softwares/SeleniumDrivers"
# driver = webdriver.Chrome()
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('C:\SSD Softwares\SeleniumDrivers\chromedriver.exe')

driver.get("https://www.w3schools.com/htmL/tryit.asp?filename=tryhtml_id_css")
driver.implicitly_wait(3)
my_element = driver.find_element(By.ID, 'getwebsitebtn')
my_element.click()
