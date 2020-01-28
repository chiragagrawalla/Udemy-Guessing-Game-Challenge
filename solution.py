import random
x=random.randint(1,100)
l=[0]
while True:
    guess=int(input("guess"))
    if (guess<1 or guess>100):
        print("OUT OF BOUND")
        continue
    else:
        l.append(guess)
    if (guess==x):
        print("Guess Correctly")
        break
    if(l[-2]==0):
        if(abs(guess-x)<10):
            print("warm")
        else:
            print("cold")
    else:
        if(abs(guess-x)<abs(guess-l[-2])):
            print("warmer")
        else:
            print("colder")
 
