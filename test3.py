import random
r = random.randint(0,10)
c = int(input("please guess the number: "))
while (r != c):
    c = int(input("pls keep guessing again till u are right: "))
    if(c == r):
        print("well done")
