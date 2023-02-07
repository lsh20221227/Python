from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
web_page = response.text
soup = BeautifulSoup(web_page,"html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
movies =movie_titles[::-1]
# 꼭봐야할 영화 100선 txt 만들기

with open("movies.txt", mode ="w", encoding='UTF8') as file:
    for movie in movies:
        file.write(f"{movie}\n")


#--------------------------------------------------------------------------------
# 라이브 웹사이트 스크래핑 하기
# response = requests.get("https://news.ycombinator.com/")
#print(response.text)
# yc_web_page = response.text
#soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
# <title>Hacker News</title>
# 1번째 기사제목 기사링크 기사추천수 찾기
#articles_tag =soup.find(name="span",class_="titleline")
#print(articles_tag)
#article_text = articles_tag.getText()
#print(article_text)
# U-Bahn station in Berlin is decorated with radioactive uranium glazed tiles (chaos.social)

#article_link = soup.find(name="a").get("href")
#article_upvote = soup.find(id="score_34691489").getText()
#article_upvote = soup.find(name="span", class_="score").getText()
#print(article_link)
#print(article_upvote)
# https://news.ycombinator.com
# 87 points

#------------------------------------------------------
#
# soup = BeautifulSoup(yc_web_page, "html.parser")
# articles=soup.find_all(class_="titleline")
# article_link = soup.find_all(name="a")[0].get("href")
# article_link 어케 가져올지 다시 생각해보기 ㅠㅠ
# ['https://news.ycombinator.com', 'news', 'newest', 'front', 'newcomments', 'ask', 'show', 'jobs', 'submit', 'login?goto=news', 'vote?id=34691489&how=up&goto=news', 'https://chaos.social/@jonty/109818563737353115', 'from?site=chaos.social', 'user?id=dewey', 'item?id=34691489', 'hide?id=34691489&goto=news', 'item?id=34691489', 'vote?id=34692190&how=up&goto=news', 'https://www.a.team//mission/the-great-betrayal', 'from?site=a.team', 'user?id=raunometsa', 'item?id=34692190', 'hide?id=34692190&goto=news', 'item?id=34692190', 'vote?id=34692137&how=up&goto=news', 'https://www.wisdomination.com/screw-motivation-what-you-need-is-discipline/', 'from?site=wisdomination.com', 'user?id=thunderbong']

# article_texts=[]
# article_links=[]
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#
#
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

#print(article_texts)
#print(article_links)
#print(article_upvotes)

# largest_number=max(article_upvotes)
# largest_index = article_upvotes.index(largest_number)
# print(largest_index)
# print(article_texts[largest_index])
#print(article_links[largest_index])


# with open("website.html",encoding='UTF8') as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# #print(soup.title)
# #print(soup.title.string)
#
# #print(soup)
# #print(soup.prettify())
# #print(soup.li)
#
# all_anchor_tags = soup.find_all(name="a")
# #print(all_anchor_tags)
#
# #for tag in all_anchor_tags:
#     #print(tag.getText())
#     #print(tag.get("href"))
#
# #heading = soup.find(name="h1", id="name")
# # print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading())
#
# # company_url = soup.select_one(selector ="p a")
# company_url = soup.select_one(selector ="#name")
# print(company_url)
# # <h1 id="name">Angela Yu</h1>
#
# headings = soup.select(".heading") # 제목 클래스를 가진 요소 선택
# print(headings)
# # [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]
