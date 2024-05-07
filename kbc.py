# lst = [["Hello",69],["xylophone","99"]]
# print(lst[0][1])

# Welcomming

wel = "Welcome To KBC"
print(wel.center(50,"~"))

Ordinals = ["1st","2nd","3rd"]

qna = [["Who is code with harry ?\na. A digital creator b. An AI c. Secret agent of government d. Alien","a" or "A" or 1],["Who made this Program ?\na. Kowalski b. Kowalski c. Kowalski d. Kowalski","a"or"b"or"c"or"d"]]

for i in qna: 
    print("Q.",i[0])
    ask = input("Enter the answer: ")
    if ask == i[1]:
        print("The answer is correct.".center(50,"~"))
    else:
        print("Your answer is wrong you lost the game go home.")
        break
    # print(i)