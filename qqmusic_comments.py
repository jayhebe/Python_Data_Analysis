from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import time


qqmusic_url = "https://y.qq.com/n/yqq/song/000xdZuV2LcQ19.html"
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_driver = webdriver.Chrome(options=chrome_options)
chrome_driver = webdriver.Chrome()
chrome_driver.get(qqmusic_url)
time.sleep(5)

# comments = chrome_driver.find_element_by_class_name("js_hot_list").find_elements_by_class_name("js_cmt_li")
# for comment in comments:
#     hot_comment = comment.find_element_by_class_name("js_hot_text")
#     print(hot_comment.text)
#     print("-" * 30)
#
# chrome_driver.close()

more_comment = chrome_driver.find_element_by_class_name("js_get_more_hot")
more_comment.click()
time.sleep(2)

comments = chrome_driver.find_element_by_class_name("js_hot_list").find_elements_by_class_name("js_cmt_li")
# print(len(comments))
for comment in comments:
    hot_comment = comment.find_element_by_class_name("js_hot_text")
    print(hot_comment.text)
    print("-" * 30)

chrome_driver.close()
