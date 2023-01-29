import requests
from datetime import datetime

pixela_endpoint = " https://pixe.la/v1/users"
USERNAME = ""
TOKEN = ""
GRAPHID="happy3"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes",
}


# response = requests.post(url=pixela_endpoint,json=user_params)
# print(response.text)
# {"message":"Success. Let's visit https://pixe.la/@sanghwa , it is your profile page!","isSuccess":true}



graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id":GRAPHID,
    "name":"Coding Graph",
    "unit":"hour",
    "type":"int",
    "color":"sora"
}

headers = {
    "X-USER-TOKEN":TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# https://pixe.la/v1/users/sanghwa/graphs/happy3.html
# UPDATE A GRAPH
update_graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
update_graph_config = {
    "id":GRAPHID,
    "name":"Coding Graph",
    "unit":"hour",
    "type":"int",
    "color":"sora"
}
#response = requests.put(url=update_graph_endpoint,json=update_graph_config,headers=headers)
#print(response.text)

#-----------------------------------------------------PIXEL ----------------------------------------------------
today = datetime.now()
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"

post_config ={
    "date":today.strftime('%Y%m%d'),
    "quantity":input("How many hour did you study today?"),
}

# CREATE A PIXEL
#response = requests.post(url=post_endpoint, json=post_config, headers=headers)
#print(response.text)


#GET A PIXEL
get_day = datetime(year=2023,month=1,day=28)
get_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{get_day.strftime('%Y%m%d')}"
#response = requests.get(url=get_endpoint, headers=headers)
#print(response.text)
# {"message":"Specified pixel not found.","isSuccess":false}
# {"quantity":"2"}

# UPDATE A PIXEL(already registered)
update_day = datetime(year=2023,month=1,day=28)
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{update_day.strftime('%Y%m%d')}"
update_config ={
    "quantity":"2",
}

# response=requests.put(url=update_endpoint,json=update_config,headers=headers)
# print(response.text)
# {"message":"Success.","isSuccess":true}


# DELETE A PIXEL
delete_day = datetime(year=2023,month=1,day=27)
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{delete_day.strftime('%Y%m%d')}"
#response = requests.delete(url=delete_endpoint,headers=headers)
#print(response.text)









