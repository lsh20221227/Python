
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = "C:\Development\chromedriver.exe"
#driver = webdriver.Chrome(executable_path = chrome_driver_path)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.python.org")

#search_bar = driver.find_element(by=By.NAME,value="q")
#print(search_bar)
# <selenium.webdriver.remote.webelement.WebElement (session="a4524a741136695f8c40b0dfea5ed0ee", element="e3c7ed7a-5292-46eb-b760-2da403e50261")>
#print(search_bar.tag_name)
#input
#print(search_bar.get_attribute("placeholder"))
#Search

#logo = driver.find_element(by=By.CLASS_NAME,value="python-logo")
#print(logo.size)
# {'height': 82, 'width': 290}

# documentation_link = driver.find_element(by=By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)
# docs.python.org

#bug_link = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
#print(bug_link.text)
# Submit Website Bug

# upcoming_time = driver.find_elements(by=By.CSS_SELECTOR,value='#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li > time')
# upcoming_name = driver.find_elements(by=By.CSS_SELECTOR,value='#content > div > section > div.list-widgets.row > div.medium-widget.event-widget.last > div > ul > li > a')


event_times = driver.find_elements(by=By.CSS_SELECTOR, value='.event-widget time')
event_names = driver.find_elements(by=By.CSS_SELECTOR, value ='.event-widget li a')
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }
print(events)

# 딕셔너리 만드는거 다시 보기



driver.quit()


