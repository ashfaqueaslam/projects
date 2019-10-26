from selenium import webdriver

browser = webdriver.Chrome(r'C:\Users\Hp\Desktop\cp\programs\chromedriver')

browser.get('https://www.seleniumhq.org')

element = browser.find_element_by_link_text('Download')
