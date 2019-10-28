from selenium import webdriver
import time


driver = webdriver.Chrome()
url = "https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php"
driver.get(url)
time.sleep(2)

username = driver.find_element_by_id("user_login")
username.send_keys("spiderman")
password = driver.find_element_by_id("user_pass")
password.send_keys("crawler334566")
btn_submit = driver.find_element_by_id("wp-submit")
btn_submit.click()
time.sleep(2)

article = driver.find_element_by_link_text("未来已来（三）——同九义何汝秀")
article.click()
time.sleep(2)

comment = driver.find_element_by_id("comment")
comment.send_keys("selenium测试测试测试123")
submit_comment = driver.find_element_by_id("submit")
submit_comment.click()

driver.close()
