from selenium import webdriver
import time 

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_tag_name('input')
    first_name.send_keys("Ivan")

    last_name = browser.find_element_by_name('last_name')
    last_name.send_keys("Petrov")

    city = browser.find_element_by_class_name('city')
    city.send_keys("Smolensk")

    country = browser.find_element_by_id('country')
    country.send_keys("Russia")

    submit_button = browser.find_element_by_xpath('//button[contains(text(), "Submit")]')
    submit_button.click()

finally:
    time.sleep(30)
    browser.quit()
