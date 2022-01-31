import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'file.txt')

    input1 = browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys("Dad")
    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys("Geek")
    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys("mail")
    input4 = browser.find_element_by_id("file")
    input4.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
