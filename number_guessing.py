from random import randint

def guess():
    while True:
        guessing_number = int(input("Enter your guessing number: "))
        random_number = randint(0, 101)

        if guessing_number == random_number:
            print("Correct, you guess collect random number!!")
            break

        if guessing_number < random_number:
            print("You guess less than the guessing number")
            continue

        if guessing_number > random_number:
            print("You guess more than guessing number")
            continue

if __name__ == '__main__':
    guess()