##Python Dictionaries

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again.",
}

#Retrieving items from dictionary.
# print(programming_dictionary["Function"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
# print(programming_dictionary)

#Loop through a dictionary
# for key in programming_dictionary:
#   print(key)
#   print(programming_dictionary[key])

#------------------------------------------------------------------------------------------------



# exercise_day_9-1
'''
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
# Solution
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] ="Outstanding"
    elif score > 80:
        student_grades[student] ="Exceeds Expectations"
    elif score > 70:
        student_grades[student] ="Acceptable"
    else:
        student_grades[student] ="Fail"


# 🚨 Don't change the code below 👇
print(student_grades)


# 혼자 해본거
student_grades={}

for key in student_scores :
    if student_scores[key]>=91:
        student_grades[key]="Outstanding"
    elif student_scores[key]>=81:
        student_grades[key]="Exceeds Expectations"
    elif student_scores[key]>=71:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)
'''


#----------------------------------------------------------------------------
#Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in a Lists

travel_log = [
{
  "country": "France",
  "cities_visited": ["Paris", "Lille", "Dijon"],
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]

#------------------------------------------------------------------------------------------------------
#exercise_day_9-2

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
# Solution
def add_new_country(country_visited, times_visited, cities_visited):
    new_country={}
    new_country["country"]=country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# print(travel_log)


# 혼자 해본거
'''
def add_new_country(a, b, c):
    travel_log.append({
    "country":a,
    "visits":b,
    "cities":c,
    })
'''

#----------------------------------------------------------------
# blind-auction-start
from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
# Solution
from replit import clear
from art import logo

print(logo)

bids = {}
bidding_finished = False


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    # bidding_record = {"Angela": 123, "James": 321}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()

'''
FAQ: My console doesn't clear()

This will happen if you’re using an IDE other than replit. 
I’ll cover how to use PyCharm in Day 15. That said, you can write your own clear() function or configure your IDE like so: 



# 혼자해본거
# 해결 X오류 : 이름과 입찰가 입력 후 새 창 나오게 하는거
# 입찰가에 숫자만 넣는게 아니라 $를 붙여서 넣어서 큰 수 비교하는거

new_party={}
def add_party(names,bids):
    new_party[names]=bids


print(art.logo_9)
print("Welcome to the secret auction program.")
end_auction=True
while end_auction:
    name=input("What is your name?: ")
    bid=int(input("What's your bid?: "))
    end=input("Are there any other bidders? Type 'yes' or 'no'.\n")
    add_party(name,bid)
    clear()
    if end=='no':
        end_auction=False

max=0
for key in new_party:
    if new_party[key]>max:
        max=new_party[key]
        max_key=key
    final={}
    final[max_key]=max

print(f"The winner is {max_key} with a bid of {max}")
'''

