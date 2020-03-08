from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    x_value = browser.find_element_by_id("input_value").text
    x_res = calc(x_value)

    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(x_res)

    browser.execute_script("window.scrollBy(0, 100);")

    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()

    radiobtn = browser.find_element_by_id("robotsRule")
    radiobtn.click()


    submit_btn = browser.find_element_by_tag_name("button")
    submit_btn.click()

finally:
    time.sleep(30)
    browser.quit()