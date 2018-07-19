# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

browser=webdriver.Chrome()
browser.implicitly_wait(10)

browser.get("https://www.duitang.com")

browser.maximize_window()

browser.find_element_by_id("dt-login").click()

browser.find_element_by_id("p-username").send_keys(u"miracle雪糕")
browser.find_element_by_id("p-password").send_keys(u"725611")

# 操作键盘
browser.find_element_by_id("p-password").send_keys(Keys.ENTER)
# browser.find_element_by_class_name("pg-loginbtn").click()

time.sleep(2)
print browser.current_url

if browser.current_url=='https://www.duitang.com/login/':
    browser.find_element_by_name("login_name").send_keys(u"miracle雪糕")
    browser.find_element_by_name("pswd").send_keys(u"725611")
    ccode=raw_input(u"请输入验证码:")
    browser.find_element_by_id("ccode").send_keys(ccode)
    browser.find_element_by_class_name("pg-lgbtn").click()
else:
    print "Login succeed!"

# 操作鼠标
time.sleep(3)
account=browser.find_element_by_id("dt-account")
ActionChains(browser).move_to_element(account).perform()

# 执行js
time.sleep(3)
js='document.getElementById("mynavtools-logout").click();'
browser.execute_script(js)


browser.quit()
