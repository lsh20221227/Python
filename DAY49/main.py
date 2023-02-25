import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
MY_EMAIL = ""
MY_PASSWORD = ""

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/jobs/search?keywords=Python%20Developer&location=%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%20%EC%84%9C%EC%9A%B8%20%EC%84%9C%EC%9A%B8&geoId=104867736&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")

# 자동로그인
login_button = driver.find_element(by=By.LINK_TEXT, value="로그인")
login_button.click()

login_email = driver.find_element(by=By.ID, value="username")
login_email.send_keys(MY_EMAIL)

login_password = driver.find_element(by=By.ID, value="password")
login_password.send_keys(MY_PASSWORD)

login_submit = driver.find_element(by=By.CSS_SELECTOR, value=".login__form_action_container button")
login_submit.click()


# 채용공고 저장 및 게시한 회사 팔로우
# time.sleep(4)
# save_click = driver.find_element(by=By.CLASS_NAME, value="jobs-save-button")
# save_click.click()

# company_click = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-unified-top-card__company-name a")
# company_click.click()
#
# time.sleep(5)
# follow_click = driver.find_element(by=By.CSS_SELECTOR, value=".org-top-card-primary-actions__inner button")
# follow_click.click()

time.sleep(4)

# 한꺼번에 지원하기

find_company = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")
for a in find_company:
    try:
        a.click()
        time.sleep(2)
        save_click = driver.find_element(by=By.CLASS_NAME, value="jobs-save-button")
        save_click.click()
        time.sleep(2)
        print("저장완료")
    except NoSuchElementException:
        print("더이상 저장할 회사가 없습니다.")
        time.sleep(10)
        driver.quit()
        continue
    except ElementClickInterceptedException:
        print("Error..")
        continue




while True:
    pass

# 오류메시지
# selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted: Element <div data-job-id="3486745317" class="job-card-container relative job-card-list











