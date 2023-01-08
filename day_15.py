MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

'''
 1 penny = 1 cent
 1nickel = 5cent
 1 dime= 10cent
 1 quarter = 25cent
 1$ = 100cent
'''

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])






'''

def remain_coin(coffees):
    cost = coffees["cost"] * 100 # 커피 가격을 cent로 변경
    quarters = float(input("How many quarters? : ")) * 25
    dimes = float(input("How many dimes? : ")) * 10
    nickles = float(input("How many nickles? : ")) * 5
    pennies = float(input("How many pennies? : "))
    cents = quarters + dimes + nickles + pennies
    if cost < cents:
        change = (cents - cost) / 100
        return change
    elif cost == cents:
        print(f"Here is your {coffee}")
    else:
        print("Sorry that's not enough money. Money refunded")

#print(MENU['espresso']["ingredients"])
# 커피별 재료

for key in MENU:
    print(MENU[key]['ingredients'])

{'water': 50, 'coffee': 18}
{'water': 200, 'milk': 150, 'coffee': 24}
{'water': 250, 'milk': 100, 'coffee': 24}


for m in resources.items():
    print(f'{m[0]} : {m[1]}')

'''


# 어떤 커피 마실래?
# report 칠경우 기계 상세내역
# 커피종류 입력시 (1) 재료가 있는지 여부 파악한 후에
# 1-1) 있을경우: 코인삽입 1-2) 없을경우 : 재료 어떤것이 없어서 안됨 . -> 재출력
# 1-1 ) 코인삽입 : 코인 몇개 넣을것인지
# 1-1-1) 코인 부족시 : 돈이 충분하지않습니다. 1-1-2) 코인이 많을시: 커피+거스름돈 1-1-3) 코인=커피: 커피대령
# 투입한 금액과 자판기 커피 가격과 비교하는 함수

# 순서를 잘짜는게 엄청 중요하다.
# 1-2) 뒤죽박죽 어떻게 해야할지 얽혀서 못건드린것같다.
# 재료충분한지 확인 -> 거래가능한지 확인 -> 커피만들기
# 내일 백지로 다시해보기














