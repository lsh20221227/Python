# Solution
from game_data import data
import random
from art import logo, vs
from replit import clear


def get_random_account():
    """Get data from random account"""
    return random.choice(data)


def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()

#####################################################################################################################

# Higher - Lower 게임 프로젝트

# A / B를 랜덤으로 고르는 모듈
# A / B follower 수 비교해서 이긴사람 return
# -> 이긴사람은 다음번에 A에서 나타나야댐
# 사용자 답변 과 비교하기
# 맞췄을 경우 출력, 틀렸을 경우 출력
# 최종 점수
# 잘못입력시 & 틀렸을때 -> "Sorry, that's wrong. Final score: {}"
# 맞췄을 경우 "You're right! Current score : {}."
# Compare A: {name},{description},{country}

import game_data
import random
import art

def random_choice():
    choice1 = random.choice(game_data.data)
    return choice1




def follower_compare(compare1, compare2):
  followerA=compare1["follower_count"]
  followerB=compare2["follower_count"]
  if followerA > followerB:
      return compare1
  else:
      return compare2




def game():
    score=0
    A=random_choice()
    while True:
        B=random_choice()
        if A==B:
            B = random_choice()
        win_follower = follower_compare(A, B)
        if win_follower == A:
            win = 'A'
        else:
            win = 'B'


        print(win)
        print(art.logo_14)
        print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}")
        print(art.vs)
        print(f"Against B: {B['name']}, {B['description']}, from {B['country']}")
        print(win)
        answer = input(f"Who has more followers? Type 'A' or 'B' : ")
        if win==answer:
            score+=1
            print(f"You're right! Current score: {score}.")
            A=win_follower
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            return

game()

########################################################################################################








