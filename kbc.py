
wel = "Welcome To KBC"
print(wel.center(50,"~"))

# Ordinals = ["1st","2nd","3rd"]

qna = [["Who is code with harry ?\na. A digital creator b. An AI c. Secret agent of government d. Alien","a" or "A" or 1],["Who made this Program ?\na. Sanyam b. Kowalski c. Harry d. Rehan","b"],["How many states of matter are there ?\na. 3 b. 4 c. 5 d. 22","d"],["What is the capital of India ?\na. Delhi b. New Delhi c. Mumbai d. None of these","b"],["The name of the pandamic started in 2019 ?\na. Plake b. Covid 19 c. Chicken Pox d. Bery Bery","b"],["What is the largest country in the world by land area?\na. China b. Russia c. United States d. Canada","b"],["What is the capital of France?\na. London b. Berlin c. Paris d. Rome","c"],["What is the tallest mountain in the world?\na. Mount Everest b. K2 c. Kangchenjunga d. Lhotse","a"],["What is the currency of Japan?\na. Euro b. Yuan c. Yen d. Dollar","c"],["What is the name of the world's largest ocean?\na. Atlantic Ocean b. Pacific Ocean c.Indian Ocean d. Arctic Ocean","b"],["What is the smallest unit of life?\na. Cell\nb. Atom\nc. Molecule\nd. Organelle","a" or "A" or 1],["What is the process by which plants make food?\na. Photosynthesis\nb. Cellular respiration\nc. Mitosis\nd. Meiosis","a" or "A" or 1],["What is the name of the Great Wall of China's original purpose?\na. To keep out wild animals\nb. To control trade routes\nc. To defend against invaders\nd. To mark the border of the empire","c" or "C" or 3],["In what century did World War II take place?\na. 18th\nb. 19th\nc. 20th\nd. 21st","c" or "C" or 3],["What is the highest mountain in the solar system?\na. Mount Everest (Earth)\nb. Olympus Mons (Mars)\nc. K2 (Earth)\nd. Mount Fuji (Japan)","b" or "B" or 2],["What is the largest desert in the world?\na. Sahara Desert\nb. Gobi Desert\nc. Arabian Desert\nd. Australian Desert","a" or "A" or 1],["Who wrote the famous play 'Hamlet'?\na. William Shakespeare\nb. Jane Austen\nc. Charles Dickens\nd. F. Scott Fitzgerald","a" or "A" or 1],["What is the name of the ring Arthur pulls from the stone in the legend of King Arthur?\na. Excalibur\nb. Anduril\nc. Narsil\nd. Glamdring","a" or "A" or 1],["What was the name of the recent space telescope launched by NASA?\na. Hubble Space Telescope\nb. James Webb Space Telescope\nc. Spitzer Space Telescope\nd. Kepler Space Telescope","b" or "B" or 2],["What is the name of the ongoing global climate change summit?\na. Paris Agreement\b. Kyoto Protocol\nc. COP28 (28th Conference of the Parties)\nd. UN Framework Convention on Climate Change","c" or "C" or 3]]

# for i in qna: 
n = 1
while n<69:
    for i in qna:
        print(f"The {n} question is :\n",i[0])
        ask = input("Enter the answer: ")
        if ask == i[1]:
            print("The answer is correct.".center(50,"~"))
            n = n+1
            # if len(qna)%6 == 0:
            #     print(f"You have won {n},000 rupees.")
            if n==len(qna):
                print("You have won won 7 crore in your fantasy.\nSo, you have made till here, checkout my other mini projects of python url - https://github.com/kowalski369/MiniPythonProjects")
                break
        else:
            print("Your answer is wrong you lost the game go home.")
            break
    if n==len(qna):
        break
    else:
        break