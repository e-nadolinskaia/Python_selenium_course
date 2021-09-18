'''
In this task, the program executes the following scenario:

1. Open a page http://suninjuly.github.io/alert_accept.html
2. Click on the button
3. Accept confirm
4. On the new page, solve a captcha for robots to get a number with the answer.
'''

from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    button = browser.find_element_by_css_selector('.btn-primary')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    text_x = browser.find_element_by_id('input_value')
    x = int(text_x.text)

    result = math.log(abs(12*math.sin(x)))

    input_answer = browser.find_element_by_id('answer')
    input_answer.send_keys(str(result))

    button = browser.find_element_by_css_selector('.btn')
    button.click()

finally:
    time.sleep(30)
    browser.quit()


