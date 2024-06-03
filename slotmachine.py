MAX_VALUE = 3
MIN_BET = 1
MAX_BET = 100


def deposit():
    while True:
        ask = input("Enter the amount $ ")
        if ask.isdigit():
            ask = int(ask)
            if ask>0:
                break
            else:
                print("The amount should be greater then 0.")
        else:
            print("Please enter a number.")
    
    return ask


def number_of_line_bet():
    while True:
       line = input("How many number of lines you want to bet on (1-"+str(MAX_VALUE)+")? ")
       if line.isdigit():
           line = int(line)
           if line>=1 and line<= MAX_VALUE:
               break
           else:
               print("Enter the line between (1 to "+str(MAX_VALUE)+")")
       else:
           print("Please enter a number.")
    
    return line


def get_bet():
    while True:
        ask = input("Enter the amount to bet on each line: ")
        if ask.isdigit():
            ask = int(ask)
            if ask>=MIN_BET and ask<=MAX_BET:
                break
            else:
                print(f"The Bet should be under ${MIN_BET}-${MAX_BET}")
        else:
            print("Please enter a number.")
    
    return ask


def main():
    balance = deposit()
    lines = number_of_line_bet()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet>MAX_VALUE:
            print(f"You don't have that much amount to bet. Your current balance is {balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines and the total bet is ${total_bet}")

main()