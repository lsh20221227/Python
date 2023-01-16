# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.read()
#     print(names)

# readlines 메소드 : 파일에 있는 각각의 줄을 포함하는 리스트를 리스트의 구성 요소로 반환해줌
# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()
#     print(names)
#   > ['Aang\n', 'Zuko\n', 'Appa\n', 'Katara\n', 'Sokka\n', 'Momo\n', 'Uncle Iroh\n', 'Toph']


#---------------------------------------------------------------------------------------------

PLACEHOLDER ="[name]"
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    contents = letter_file.read()
    for name in names:
        strip_name = name.strip()
        new_letter = contents.replace(PLACEHOLDER,strip_name)
        with open(f"./Output/ReadyToSend/letter_for_{strip_name}.txt",mode="w") as complete:
            complete.write(new_letter)


