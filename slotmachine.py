# This project is made by watching the tutorial from youtube tutorial link - https://youtu.be/th4OBktqK1I?si=F9vNyzPI-YgMD9uD  
import random

MAX_VALUE = 3
MIN_BET = 1
MAX_BET = 100

ROWS = 3
COLS = 3

symbol_count = {
    "A":2,
    "B":4,
    "c":6,
    "D":8
}

symbol_value = {
    "A":5,
    "B":4,
    "c":3,
    "D":2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0 
    winning_line = []
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_line.append(line+1)
        
    return winnings, winning_line



def get_slot_machine_spin(rows,cols,symbols):
    all_symbol = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols =all_symbol[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):# transposing the column
    for row in range(len(columns[0])):
        for  i, column in enumerate(columns):
            if i != len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        
        print()


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

def spin(balance):
    lines = number_of_line_bet()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet>MAX_BET:
            print(f"You don't have that much amount to bet. Your current balance is {balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines and the total bet is ${total_bet}")
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings, winning_line =check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print(f"You won on lines",*winning_line) # asterisk is used as unpack or splat oprator to unpack
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Please press enter to play (q to quit.)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()