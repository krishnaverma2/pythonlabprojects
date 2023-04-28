import random
print("Your OTP is : ")
out=random.random()
otp=str(out)
otp2=otp[2:6]
print("Your otp is",otp2)
while 3:
    g=input("Enter m for more otps and n for no more otps")
    if g=='m':
     out1=random.random()
     otp1=str(out1)
     otp3=otp1[2:6]
     print('Your otp is',otp)
    else:
     print("Thanks for using our otp generator")
     sbreak
    
