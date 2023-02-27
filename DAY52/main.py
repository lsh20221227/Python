from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.common.exceptions import ElementClickInterceptedException


USERNAME = ""
PASSWORD = ""

class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        self.user_name = self.driver.find_element(by=By.NAME, value='username')
        self.user_name.send_keys(USERNAME)
        self.user_password =self.driver.find_element(by=By.NAME, value='password')
        self.user_password.send_keys(PASSWORD)
        self.user_password.send_keys(Keys.ENTER)
        time.sleep(3)



    def find_followings(self):
        time.sleep(2)

        self.driver.get(f"https://www.instagram.com/{USERNAME}/")
        time.sleep(2)
        self.following = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[3]/a')
        self.following.click()

        time.sleep(3)
        scroll = self.driver.find_element(by=By.XPATH,
                                          value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]')
        for i in range(5):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            time.sleep(1)


    def follow(self):
        follows = self.driver.find_elements(by=By.CSS_SELECTOR, value='._aano button')
        for follow in follows:
            try:
                follow.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
                cancel.click()


bot = InstaFollower()
bot.login()
bot.find_followings()
bot.follow()

while True:
    pass

