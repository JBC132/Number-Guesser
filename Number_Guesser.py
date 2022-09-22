import random

upto = input("Type a number: ")

if upto.isdigit():
    upto = int(upto)

    if upto <= 0:
        print("Type in number larger than 0.")
        quit()

else:
    print("Type in number.")
    quit()

random_number = random.randint(0, upto)


while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Type in number.")
        continue

    if user_guess == random_number:
        print("-----Correct.-----")
        break
    
    else:
        print("------Wrong.------")