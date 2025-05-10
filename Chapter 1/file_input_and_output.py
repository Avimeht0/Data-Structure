f=open("poem.txt","r")
data=f.read()
if "time" in data :
    print(f, "the word 'time' is present in the file \"poem.txt\"")
f.close()


import random

def game():
    print("you are plying a  the game ")
    score=random.randint (1, 100)
    with open("Hiscore.txt",) as f:
        Hiscore=f.read()
        if Hiscore!="":
            Hiscore=int(Hiscore)
        else:
            Hiscore=0
    print (f"your score is  {score}")

    if score>Hiscore:
        print(f"you have a new high score is {score}")
        with open("Hiscore.txt","w") as f:
            f.write(str(score))
    return score


game()