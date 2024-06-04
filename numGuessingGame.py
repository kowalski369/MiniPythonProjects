# this program gernerates a random number and we have to guess the number
import random


def main():
    num = random.randint(1,100)
    while True:
        ask = int(input("Guess the number: "))
        if ask == num:
            print("Yes!!!!!!, Your guess is right.")
            break
        else:
            print(f"The number is around {num+10} to {num-10}")


main()