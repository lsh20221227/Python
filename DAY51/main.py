from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = ""
TWITTER_PASSWORD =""

class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.down=0
        self.up=0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_click = self.driver.find_element(by=By.CSS_SELECTOR, value=".start-button a")
        go_click.click()
        time.sleep(60)
        self.driver.find_element(by=By.LINK_TEXT, value="")
        self.down = self.driver.find_element(by=By.CLASS_NAME, value="download-speed").text
        print(f"down: {self.down}")
        self.up = self.driver.find_element(by=By.CLASS_NAME, value="upload-speed").text
        print(f"up: {self.up}")
        time.sleep(10)

    def tweet_login(self):
        time.sleep(2)
        self.driver.get("https://twitter.com/?lang=ko")
        time.sleep(1)
        self.login = self.driver.find_element(by=By.LINK_TEXT, value="로그인")
        self.login.click()
        time.sleep(2)
        self.email = self.driver.find_element(by=By.CSS_SELECTOR, value=".r-qvutc0 input")
        self.email.send_keys(TWITTER_EMAIL)
        self.email.send_keys(Keys.ENTER)
        time.sleep(2)
        self.password = self.driver.find_element(by=By.NAME, value="password")
        self.password.send_keys(TWITTER_PASSWORD)
        self.password.send_keys(Keys.ENTER)
        time.sleep(2)

    def tweet_at_provider(self):
        time.sleep(2)
        #tweet_input=self.driver.find_element(by=By.CLASS_NAME, value="DraftEditor-editorContainer")
        tweet_input=self.driver.find_element(by=By.CLASS_NAME, value="public-DraftEditor-content")
        tweet_input.send_keys(f"My internet speed {self.down}down / {self.up}up ")
        tweet_send = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_send.click()
        time.sleep(10)
        self.driver.quit()





my_internet = InternetSpeedTwitterBot()
my_internet.get_internet_speed()
my_internet.tweet_login()
my_internet.tweet_at_provider()

while True:
    pass







