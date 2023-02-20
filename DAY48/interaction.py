from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://en.wikipedia.org/wiki/Main_Page')
article_count = driver.find_element(by=By.CSS_SELECTOR, value='#articlecount a')
#article_count.click()

all_portals = driver.find_element(by=By.LINK_TEXT, value='Wikibooks')
#all_portals.click()

search = driver.find_element(by=By.NAME, value='search')
search.send_keys('Python')
search.send_keys(Keys.ENTER)


driver.quit()
