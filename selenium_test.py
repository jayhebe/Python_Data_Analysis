from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://localprod.pandateacher.com/python-manuscript/hello-spiderman/")
time.sleep(2)

teacher = driver.find_element_by_id("teacher")
teacher.send_keys("你爸爸")
assistant = driver.find_element_by_id("assistant")
assistant.send_keys("你大爷")
time.sleep(1)
button = driver.find_element_by_class_name("sub")
button.click()
time.sleep(2)
driver.close()
