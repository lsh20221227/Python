import requests
from datetime import datetime
import os


exercise_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
API_ID= os.environ.get("EXERCISE_ID")
API_KEY=os.environ.get("EXERCISE_KEY")

WEIGHT = 58
HEIGHT = 158
AGE = 29
input_exercise =input("Tell me which exercises you did: ")

new_query ={
    "query":input_exercise ,
    "gender":"female",
    "weight_kg":WEIGHT,
    "height_cm":HEIGHT,
    "age":AGE,

}
headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=exercise_endpoint, json=new_query,headers=headers)
data = response.json()
# print(data['exercises'])


#-------------SHEET
sheety_endpoint = os.environ.get('SHEETY_ENDPOINT')
today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%X")
for a in data['exercises']:
    post_sheet = {
        "workout":{
            "date":date,
            "time":time,
            "exercise":a["name"],
            "duration":a["duration_min"],
            "calories":a["nf_calories"],
        }
    }


auth = (
    os.environ.get('AU_NAME'),
    os.environ.get('AU_PASS')
)
###----------- GET
# response = requests.get(url=sheety_endpoint)
# result = response.json()
# print(result)

###------------ POST
# response =requests.post(url=sheety_endpoint,json=post_sheet)
# print(response.text)

response = requests.post(url=sheety_endpoint,json=post_sheet,auth=auth)
print(response.text)

# Tell me which exercises you did: 20 HOURS running
# {
#   "workout": {
#     "date": "30/01/2023",
#     "time": "23:21:12",
#     "exercise": "running",
#     "duration": 1200,
#     "calories": 11368,
#     "id": 11
#   }
# }



