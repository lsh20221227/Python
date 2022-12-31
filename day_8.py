#Write your code below this line 👇
'''
def paint_calc(height, width, cover):
    wall = (height*width)
    if wall % coverage ==0:
        cans = int(wall / coverage)
    else:
        cans = int(wall / coverage) +1
    print(cans)


#Solution
import math

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint")

#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
'''

#--------------------------------------------------------------
# 소수 확인기 ( 8 - 2 - exercise )

# Write your code below this line 👇

'''def prime_checker(number):
    count=0
    for i in range(2,number):
        if number % i == 0:
            count+=1
        else:
            count+=0

    if count==0 :
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Solution
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("It's not a prime number")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
'''

#--------------------------------------------------------------------------------
# 카이사르 암호화(1부)
'''
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(text, shift):
# Solution -----------------------------------------------
def encrypt(plain_text,shift_amount):
    cipher_text=""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text+=new_letter
    print(f"The encoded text is {cipher_text}")
    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text'
    # forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

# 혼자 해본거 ------------------------------------------------------------

def encrypt(text, shift):
    text_encode = []
    for i in text:
        a = alphabet.index(i)
        text_encode.append(a)

    text_decode = []

    for i in text_encode:
        encode_number = i + shift
        text_decode.append(encode_number)

    text_de = []
    for i in text_decode:
        text_de += alphabet[i]
    print(text_de)
    
    if  new_position>len(alphabet)-1:
        new_position=new_position-len(alphabet)


    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    # index가 26을 넘어가면 오류가 발생할텐데 어떻게 해결하는지
    # 여러가지 Solution이 있지만, 코드를 바꾸지않고 하는 방법으로 기존에있는 알파벳 리스트에서 추가적으로 더 추가하니 오류없이 해결됨
#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
encrypt(plain_text=text, shift_amount=shift)

#----------------------------------------------------------------------------------
# 복호화(2부)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# Solution
def decrypt(cipher_text, shift_amount):
    plain_text=""
    for letter in cipher_text:
        position=alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print("The decoded text is {plain_text}")

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
  #e.g.
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable. You should be able to test the code to encrypt *AND* decrypt a message.
if direction=="encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction=="decode":
    decrypt(cipher_text=text, shift_amount=shift)


# -----------------------------------------------------------------------------------------
# 혼자해본거

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

def decrypt(de_text, de_shift):
    decode_text = ""
    for i in de_text:
        position = alphabet.index(i)
        new_position = position - de_shift
        decode_text += alphabet[new_position]
    print(f"The decoded text is {decode_text}")
      
if direction=="encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction=="decode":
    decrypt(text, shift)


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 카이사르 암호 3부 
# 코드 재구성
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# Solution
# TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar().
def caesar(start_text, shift_amount, cipher_direction):
    end_text=""
    if cipher_direction == "decode":
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)

        new_position = position + shift_amount
        end_text+=alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")
# TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text=text,shift_amount=shift, cipher_direction=direction)


#-----------------------------------------------------------------------------------------------------------------------------------------------
# 혼자해본거

def caesar(ca_text, ca_shift, ca_direction):
    if ca_direction=="encode":
        encode_text=''
        for i in ca_text:
            position=alphabet.index(i)
            new_position=position+ca_shift
            encode_text+=alphabet[new_position]
    elif ca_direction=="decode":
        caesar(ca_text=text,ca_shift=shift,ca_direction=direction)
        decode_text=''
        for j in ca_text:
            position = alphabet.index(j)
            new_position = position - ca_shift
            decode_text+=alphabet[new_position]

    if ca_direction=="encode":
        print(f"The encode text is {encode_text}")
    elif ca_direction=="decode":
        print(f"The decoded text is {decode_text}")
'''

#------------------------------------------------------------------------------------------------
# 카이사르 암호 4단계
# 유저 경험 개선 & 마무리

# Solution
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.
should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  #TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
  #Try running the program and entering a shift number of 45.
  #Add some code so that the program continues to work even if the user enters a shift number greater than 26.
  #Hint: Think about how you can use the modulus (%).
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")


#-------------------------------------------------------------------------------------------------
# 혼자 해본거
'''
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if shift_amount >= 26:
        shift_amount=shift_amount % 26
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char not in alphabet:
            end_text += char
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]

    print(f"Here's the {cipher_direction}d result: {end_text}")

print(art.logo)

end_game=True
while end_game:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    type=input("Type 'yes' if you want to go again. Other wise type 'no'.\n")
    if type=="no":
        print("Good bye")
        end_game=False

'''




