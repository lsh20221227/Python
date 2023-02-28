from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
# 요청헤더 : https://myhttpheader.com/
Q_LINK = "https://docs.google.com/forms/d/e/1FAIpQLScgyL61vorwfwllP5K5dqj0KbaWdN2SpxTJTdAILeLlMW8gsw/viewform?usp=sf_link"

header = {
    "User-Agent":"",
    "Accept-Language":"",
}

response = requests.get(URL,headers=header)
web_page = response.text
soup = BeautifulSoup(web_page,"html.parser")


all_data = soup.select("#grid-search-results > ul a")
link_list = []
for data in all_data:
    links = data["href"]
    if "https" not in links:
        links = f"https://www.zillow.com{links}"
    link_list.append(links)

#print(f"링크는 {link_list}")

all_juso = soup.select("#grid-search-results > ul address")
juso_list = [data.getText().split('|')[-1] for data in all_juso]
#print(f"주소는 {juso_list}")

all_price = soup.select("#grid-search-results > ul li div span")
price_list = [data.getText() for data in all_price if "$" in data.text]
#print(f"가격은 {price_list}")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for n in range(len(link_list)):
    driver.get(Q_LINK)
    time.sleep(3)

    #juso_1 = driver.find_element(by=By.XPATH, value='/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    juso_1 = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    juso_1.send_keys(juso_list[n])

    #price_2 = driver.find_element(by=By.XPATH, value='/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_2=driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_2.send_keys(price_list[n])


    #link_3 = driver.find_element(by=By.XPATH, value='/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_3 = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_3.send_keys(link_list[n])

    #submit_button = driver.find_element(by=By.XPATH, value='/html/body/div/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()

while True:
    pass



