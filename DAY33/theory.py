import requests
from datetime import datetime

# https://sunrise-sunset.org/api
MY_LAT = 37.566536
MY_LONG = 126.977966

# ISS가 내 위치 근처에있는지 확인하는 함수
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]['longitude'])
    iss_longitude = float(data["iss_position"]['longitude'])
    # Your position is within +5 or -5 degrees of the iss position.

    if MY_LAT - 5<= iss_latitude <= MY_LAT +5 and MY_LONG -5 <= iss_longitude <= MY_LONG + 5:
        return True

# print(response)
# <Response [200]>

# response = requests.get(url="http://api.open-notify.org/is-now.json")
# print(response.status_code)
# 404

#data = response.json()["iss_position"]
# {'longitude': '112.1892', 'latitude': '46.2423'}
# longitude = response.json()["iss_position"]['longitude']
# latitude = response.json()["iss_position"]['latitude']

# iss_position = (longitude, latitude)
# print(iss_position)

#---------------------------------------------------------------------------------

# https://sunrise-sunset.org/api
# MY_LAT = 37.566536
# MY_LONG = 126.977966

# Your position is within +5 or -5 degrees of the iss position.
# if MY_LAT - 5<= iss_latitude <= MY_LAT +5 and MY_LONG -5 <= iss_longitude <= MY_LONG + 5:


# 밤시간인지 아닌지 확인하는 함수


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted" :0,
    }

    reponse = requests.get(" https://api.sunrise-sunset.org/json",params=parameters)
    reponse.raise_for_status()
    data = reponse.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
        # 하늘이 어둡다.


# print(data)
# https://api.sunrise-sunset.org/json?lat=37.566536&lng=126.977966
# Chrome 에 JSON VIEW 설치 후 입력시 정돈된 json 파일



# print(sunrise) # 12시간 형식
# 2023-01-24T22:39:44+00:00
# print(sunrise.split("T")[1].split(":")[0]) # 일출시각
# print(sunset.split("T")[1].split(":")[0]) # 일몰시각
# 22
# time_now = datetime.now()
# print(time_now) # 24시간 형식 -> 12시간으로 변경 (parameter에 선택매개변수인 formatted 추가)
# print(time_now.hour) # 현재 시계 시각




