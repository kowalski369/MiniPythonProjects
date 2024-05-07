import time

time = int(time.strftime("%H"))
# print(type(time))

# alloting time when to greet

match time:
    case _ if time<12 and time>=4 :
        print("Good Morning Sir.")
    case _ if time>=12 and time<16 :
        print("Good Afternoon Sir.")
    case _ if time>=16 and time<21:
        print("Good Evening Sir.")
    case _ if time>21 and time>00:
        print("Good Night Sir.")
    case _ if time>0 and time<4 :
        print("What the hell are you doing in this time, go to sleep.")


