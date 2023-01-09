#import turtle
#from turtle import Turtle, Screen

#timmy = turtle.Turtle()
#timmy = Turtle()
#print(timmy)
#timmy.shape("turtle")
#timmy.color("coral")
#timmy.forward(100)

#my_screen = Screen()
#print(my_screen.canvheight)
#my_screen.exitonclick()
'''
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])\


+--------------+----------+
| Pokemon Name |   Type   |
+--------------+----------+
|   Pikachu    | Electric |
|   Squirtle   |  Water   |
|  Charmander  |   Fire   |
+--------------+----------+

종료 코드 0(으)로 완료된 프로세스

'''
# print(table.align)
# {'base_align_value': 'c', 'Pokemon Name': 'c', 'Type': 'c'}
# table.align = "l"
# print(table)

#------------------------------------------------------------------
# 1. Print report.
# 2. Check resources sufficient?
# 3. Process coins.
# 4. Check transaction successful?
# 5. Make Coffee.



from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)

        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)




########################################################################################################################
'''
menu=Menu()
machine = MoneyMachine()
coffeemaker = CoffeeMaker()
#items = Menu.get_items(menu)
choice = input(f"What would you like? : ")
ingredient=menu.find_drink(choice)
print(menu.get_items(),ingredient)


if choice == "report":
    coffeemaker.report()
else:
    print(menu.get_items())
    find = menu.find_drink(choice)


'''

'''
get_item=menu.get_items()
choice = input(f"What would you like? : ")
menu_choice=menu.find_drink(choice)

#items = MenuItem(menu_choice,water=,milk=,coffee=,cost=)

continuee=True
while continuee:
    if choice == "report":
        coffeemaker.report()
    elif choice == "off":
         continuee=False
    else:
        global coffeemaker
        if coffeemaker.is_resource_sufficinet(choice):

'''















