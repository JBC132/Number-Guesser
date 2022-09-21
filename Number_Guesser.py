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


