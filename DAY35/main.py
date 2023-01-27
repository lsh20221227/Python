import requests

# OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"
# https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
# http://jsonviewer.stack.hu/


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# api_key = ""


parameter = {
    "lat" :37.566536,
    "lon" :126.977966,
    "appid": api_key,
    "exclude" : "current,minutely,daily" # 시간대별 예보만 받기위해 나머지 제거

}

response = requests.get(OWM_Endpoint, params=parameter)
print(response.status_code)
weather_data = response.json()
# weather_data["hourly"][0]["weather"][0]["id"]

weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella. ")





