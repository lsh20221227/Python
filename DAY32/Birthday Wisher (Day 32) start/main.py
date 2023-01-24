# import smtplib
# #
# my_email = "pythontesting73@gmail.com"
# password = "pythonsmtp!!"
#
#
# with smtplib.SMTP("smtp.gmail.com",587) as connection:
#
#     connection.starttls()
#     connection.login(user = my_email,password=password )
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="steadyeffort20@yahoo.com",
#                         msg="Subject:Hello\n\nThis is the body of my email")


import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
print(day)
# print(day_of_week)
# print(type(now))

date_of_birth = dt.datetime(year=1994 ,month=5, day=14 , hour=16)
# print(date_of_birth)

import random

with open("quotes.txt") as data:
    quotes = data.read()

quotes = quotes.split('"')
random_quotes = random.choice(quotes)
print(random_quotes)


