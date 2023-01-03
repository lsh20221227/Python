#Function with Outputs

'''
def format_name(f_name,l_name):
    """Take a first and last name and format it 
    to return the title case version of the name.""" #독스트링
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("AnGELA","YU")
# print(formated_string)
# print(format_name("AnGELA","YU"))

#-------------------------------------------------------------------------------
# day-10-1-exercise
# Solution
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year,month):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]

# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

##################################################
# 혼자 해본거

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year)==True:
        month_days[1]=29
    return month_days[month-1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


#----------------------------------------------------------------
# Calculator

# Add
def add(n1, n2):
    return n1 + n2
# Substract
def substract(n1, n2):
    return n1 - n2
# Multiply
def multiply(n1, n2):
    return n1 * n2
# Divide
def divide(n1, n2):
    return n1 / n2

# Dictonary 만들기 (Key : +,-,*,/) (Value : 각각의 함수)
# Solution
# add(num1, num2) 로 안해줘도 된당 신기
operations ={
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number?: "))
for symbol in operations:
    print(symbol)


#Here we select "+"
operation_symbol = input("Pick an operation: ")
num2 = int(input("What's the next number?: "))
calculation_function = operations[operation_symbol]
first_answer = calculation_function(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {first_answer}")

#Here we select "*" which overides the "+" we selected on line 26.
operation_symbol = input("Pick an operation: ")
num3 = int(input("What's the next number?: "))

#Here the calculation_function selected will be the multiply() function
calculation_function = operations[operation_symbol]

#Here the code will be:
#second_answer = multiply(multiply(num1, num2), num3) ★★★★
second_answer = calculation_function(calculation_function(num1, num2), num3)
#second_answer = 2 * 3 * 3 = 18
#To fix this bug we need to change the code on line 42 to:
second_answer = calculation_function(first_answer, num3)
#In the next lesson, we will delete all the code from line 34-48 so don't worry
#It won't affect your final project.
#But it's a good oportunity to practice debugging. 🐞

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")

##########################################################

def calculation(a):
    if a=="+":
        result = add(num1,num2)
    elif a=="-":
        result = substract(num1,num2)
    elif a=="*":
        result = multiply(num1,num2)
    elif a=="/":
        result = divide(num1,num2)
    return result
answer = calculation(operation_symbol)

#############################################################
#------------------------------------------------------------------------------
# 재귀 함수
def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo_10)

    num1 = int(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator() # 재귀함수 : 특정 조건을 설정하지 않을 시 무한 반복 유의

calculator()
'''

#-------------------------------------------------------------------------------
# 소수점을 입력하면 프로그램 오류가 나타나며 종료되는 버그 해결 생각해보기

from replit import clear
from art import logo_10

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(logo_10)

    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            clear()
            calculator() # 재귀함수 : 특정 조건을 설정하지 않을 시 무한 반복 유의

calculator()
