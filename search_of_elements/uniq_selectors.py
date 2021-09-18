from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element_by_css_selector("input.first[required]")
    first_name.send_keys('Kate')

    last_name = browser.find_element_by_css_selector('input.second[required]')
    last_name.send_keys('Korvusova')

    email = browser.find_element_by_css_selector('input.third[required]')
    email.send_keys('@gmail.com')

    submit_button = browser.find_element_by_css_selector("button.btn")
    submit_button.click()

    time.sleep(5)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()
