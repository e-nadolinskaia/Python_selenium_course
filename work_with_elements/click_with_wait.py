from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import math
from selenium.webdriver.support.ui import WebDriverWait



browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/explicit_wait2.html')

button = browser.find_element_by_css_selector('.btn')
browser.execute_script('return arguments[0].scrollIntoView(true);',button)

price = WebDriverWait(browser,10).until(
    ec.text_to_be_present_in_element((By.ID, 'price'),'$100')
    )
button.click()

x_text = browser.find_element_by_id('input_value')
x = int(x_text.text)
result = math.log((abs(12*math.sin(x))))
input = browser.find_element_by_tag_name("input")
browser.execute_script("return arguments[0].scrollIntoView(true);", input)
input.send_keys(str(result))

button_send = browser.find_element_by_id('solve')
button_send.click()

