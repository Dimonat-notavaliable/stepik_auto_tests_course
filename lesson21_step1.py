from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    link = "https://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x = browser.find_element_by_id("input_value").text
    input1 = browser.find_element_by_id("answer")
    input1.send_keys(str(math.log(abs(12 * math.sin(int(x))))))
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    button.click()

finally:
    time.sleep(10)
    browser.quit()
