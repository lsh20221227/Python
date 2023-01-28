import requests
import datetime

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
parameter ={
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":"TSLA",
    "apikey": "",
}

news_parameter = {
    "q" : "tesla",
    "from" : "2023-01-27",
    "sortBy" : "publishedAt",
    "apiKey" : "",

}

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tdby = yesterday - datetime.timedelta(days=1)
today = str(today)
yesterday = str(yesterday)

## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(url=STOCK_ENDPOINT,params=parameter)
stock_data = response.json()
closing = [ value  for (key,value) in stock_data['Time Series (Daily)'][f"{yesterday}"].items()][3]
yesterday_close = float(closing)
#TODO 2. - Get the day before yesterday's closing stock price
closing2 = [ value2  for (key2,value2) in stock_data['Time Series (Daily)'][f"{tdby}"].items()][3]
tdby_close = float(closing2)
#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
stock_diff = tdby_close - yesterday_close
abs_stock = abs(stock_diff)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percent_stock = abs_stock / tdby_close * 100

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
def get_news():
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
    news_data = news_response.json()
    return news_data

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percent_stock > 10:
    print("Get News")
    news_data = get_news()
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

# TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    article = []
    article += news_data["articles"][:3]
    #print(article)
    # [{'source': {'id': None, 'name': 'Biztoc.com'}, 'author': 'u.today', 'title': "Dogecoin Community Stunned by McDonald's Refusal to Go Viral With DOGE", 'description': "Member of DOGE army says that by beginning to accept Dogecoin McDonald's can go viral Dogecoin fan @DogeDillionaire, one of the DOGE army members, believes that Elon Musk could help McDonald's expand its customer base and go viral, at least for one of its pro…", 'url': 'https://biztoc.com/x/046d93b1e7f09a1e', 'urlToImage': 'https://c.biztoc.com/p/046d93b1e7f09a1e/og.webp', 'publishedAt': '2023-01-28T11:48:05Z', 'content': "Member of DOGE army says that by beginning to accept Dogecoin McDonald's can go viralDogecoin fan @DogeDillionaire, one of the DOGE army members, believes that Elon Musk could help McDonald's expand … [+302 chars]"}, {'source': {'id': None, 'name': 'Ambcrypto.com'}, 'author': 'Suzuki Shillsalot', 'title': 'Bitcoin (BTC) Price Prediction 2025-2030: Will BTC’s sideways market continue', 'description': 'Disclaimer: The datasets shared in the following article have been compiled from a set of online resources and do not reflect AMBCrypto’s own research on the subject With Bitcoin’s (BTC) trading volume rocketing beyond $40 billion, the digital asset’s price h…', 'url': 'https://ambcrypto.com/bitcoin-btc-price-prediction-18/', 'urlToImage': 'https://ambcrypto.com/wp-content/uploads/2023/01/btc-fi-1000x600.jpg', 'publishedAt': '2023-01-28T11:45:57Z', 'content': 'Disclaimer: The datasets shared in the following article have been compiled from a set of online resources and do not reflect AMBCryptos own research on the subject\r\nWith Bitcoin’s (BTC) trading volu… [+20245 chars]'}, {'source': {'id': 'business-insider', 'name': 'Business Insider'}, 'author': 'tlevin@insider.com (Tim Levin)', 'title': "I was obsessed with my Tesla but Elon Musk convinced me I'd rather drive an electric Mercedes-Benz", 'description': "Christine Orita got her first Tesla in 2013. Elon Musk's conservative views and promises about self-driving tech pushed her to ditch the brand.", 'url': 'https://www.businessinsider.com/tesla-owner-traded-model-s-mercedes-eqs-elon-musk-twitter-450-2023-1', 'urlToImage': 'https://i.insider.com/63d2bf38b1f17f001805d135?width=1200&format=jpeg', 'publishedAt': '2023-01-28T11:45:00Z', 'content': 'This as-told-to essay is based on a conversation with Christine Orita, 65, a longtime Tesla owner from California who recently decided to ditch her 2020 Model S for an electric Mercedes-Benz. Her wor… [+4478 chars]'}]


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

    final = [f"TITLE : {a['title']} URL: {a['url']}" for a in article]
    print(final)
    # ["TITLE : Dogecoin Community Stunned by McDonald's Refusal to Go Viral With DOGE URL: https://biztoc.com/x/046d93b1e7f09a1e", 'TITLE : Bitcoin (BTC) Price Prediction 2025-2030: Will BTC’s sideways market continue URL: https://ambcrypto.com/bitcoin-btc-price-prediction-18/', "TITLE : I was obsessed with my Tesla but Elon Musk convinced me I'd rather drive an electric Mercedes-Benz URL: https://www.businessinsider.com/tesla-owner-traded-model-s-mercedes-eqs-elon-musk-twitter-450-2023-1"]

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

