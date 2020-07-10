
from selenium.webdriver import Chrome, ChromeOptions
import time

option = ChromeOptions()
option.add_argument("--headless")   # 隐藏浏览器
option.add_argument("--no-sandbox")

browser = Chrome(options=option)
url = ""
browser.get(url)
buttern = browser.find_element_by_css_selector(r'')
buttern.click()
time.sleep(1)

content = browser.find_elements_by_xpath(r'')
for c in content:
    print(c.text)
browser.close()
