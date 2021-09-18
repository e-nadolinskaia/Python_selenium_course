from selenium import webdriver
import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/math.html')

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    text_input = browser.find_element_by_id('answer')
    text_input.send_keys(y)

    option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    option1.click()

    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()

    button = browser.find_element_by_css_selector(".btn.btn-default")
    button.click()

finally:
    time.sleep(30)
    browser.quit() 
     



