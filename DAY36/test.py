import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
print(today)
str(today)
print(today)
print(yesterday)

a = 179
b = 160


diff = (abs(b-a))
abss = diff / a * 100


print(abss)
