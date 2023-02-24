from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(by=By.ID,value='cookie')


price = [] # 아이템 가격 list
items = [] # 아이템 이름 list

# print(int(moni.text.split('-')[1]))

purchase_price = 0
timeout = time.time()+5
finish = time.time()+ 60*2
while True:
    cookie.click()

    if time.time() > timeout:

        # 쿠키 갯수
        count = driver.find_element(by=By.ID, value='money').text
        if ',' in count:
            count = count.replace(',','')
        counts = int(count)  # 쿠키 갯수

        #아이템 상점
        moni = driver.find_elements(by=By.CSS_SELECTOR, value='#store b')  # 아이템 상점
        for e in moni:
            if e.text != "":
                price.append(int(e.text.split('-')[1].replace(',', '')))
                items.append(e.text.split('-')[0].strip())

        stores = {p:i for p, i in zip(price,items)}


        can=[]
        for i in price:
            if counts > i:
                can.append(i)


        max=0
        for i in can:
            if i > max:
                max = i

        max_buy = stores[max] # 구매할수있는 가장 큰 가격의 상품명

        click_buy = "buy"+ max_buy

        max_buy = driver.find_element(by=By.ID, value=click_buy)
        max_buy.click()

        timeout = time.time()+5

    if time.time() > finish:
        cps = driver.find_element(by=By.ID, value="cps").text
        print(f"1초당 쿠키 개수 : {cps}")
        break

driver.quit()



# https://gist.github.com/angelabauer/affb3ce61bc79ada90dea26052c27c2b
