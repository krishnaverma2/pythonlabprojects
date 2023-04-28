import random
name=input("Enter your name : ")
print('You have 3 chances to guess a number')
i=3
while(i):
    num=int(input("enter the number"))
    out=random.randrange(1,100)
    if num==out:
        print("Wooahh" ,name, " You are champion")
        break
    elif(num<out):
        print("Sorry" ,name, " your number is small")
    else:
        print("Sorry" ,name ,"Your number is large")
    i-=1;
