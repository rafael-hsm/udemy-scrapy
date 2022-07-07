from random import randint

number = randint(0, 100)
r = "Y"

while r != "N":
    try:
        tip = int(input("Enter a number between 0 - 100: "))
        difference = number - tip
        if difference == 0:
            print("*" * 20)
            print("YOU WIN".center(20))
            print(f"The number is {number}")
            print("*" * 20)
            break
        elif 0 < abs(difference) < 10:
            print("You're wrong, but you are close.")

        elif 9 < abs(difference) < 100:
            print("You're wrong, the difference is greater than 10, try again.")
        r = input("Do you try again [Y/N]? ").upper()

    except ValueError:
        print("Type a number like 10")

    except KeyboardInterrupt:
        print("You decide interrupt the code manually.")
