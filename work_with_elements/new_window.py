'''
Task:
1. Open a page http://suninjuly.github.io/redirect_accept.html
2. Click on the button
3. Switch to a new tab
4.Pass the captcha for the robot and get the answer number.
'''

from selenium import webdriver
import math
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    button = browser.find_element_by_css_selector('.trollface')
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_in_text = browser.find_element_by_id('input_value')
    x = int(x_in_text.text)

    result = math.log(abs(12*math.sin(x)))
    

    input_result = browser.find_element_by_id('answer')
    input_result.send_keys(str(result))

    button = browser.find_element_by_css_selector('.btn')
    button.click()

    answer = browser.switch_to.alert
    print(answer.text)

finally:
    time.sleep(10)
    browser.quit()
