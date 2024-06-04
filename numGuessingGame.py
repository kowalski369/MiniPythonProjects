# this program gernerates a random number and we have to guess the number
import random


def main():
    num = random.randint(1,100)
    while True:
        around = random.randint(1,20)
        ask = int(input("Guess the number: "))
        if ask == num:
            print("Yes!!!!!!, Your guess is right.")
            break
        else:
            print(f"The number is around {num+around} to {num-around}")


main()