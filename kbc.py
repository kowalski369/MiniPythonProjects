
wel = "Welcome To KBC"
print(wel.center(50,"~"))

# Ordinals = ["1st","2nd","3rd"]

qna = [["Who is code with harry ?\na. A digital creator b. An AI c. Secret agent of government d. Alien","a" or "A" or 1],["Who made this Program ?\na. Sanyam b. Kowalski c. Harry d. Rehan","b"],["How many states of matter are there ?\na. 3 b. 4 c. 5 d. 22","d"],["What is the capital of India ?\na. Delhi b. New Delhi c. Mumbai d. None of these","b"],["The name of the pandamic started in 2019 ?\na. Plake b. Covid 19 c. Chicken Pox d. Bery Bery","b"],]

# for i in qna: 
n = 1
while n<69:
    for i in qna:
        print(f"The {n} question is :\n",i[0])
        ask = input("Enter the answer: ")
        if ask == i[1]:
            print("The answer is correct.".center(50,"~"))
            n = n+1
            if len(qna)%6 == 0:
                print(f"You have won {n},000 rupees.")
            if n==len(qna)+1:
                break
        else:
            print("Your answer is wrong you lost the game go home.")
            break
    if n==len(qna)+1:
        break
    else:
        break