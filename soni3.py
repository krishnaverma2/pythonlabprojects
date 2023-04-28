import random
print("Your OTPs are : ")
for i in range(10):
    out=random.random()
    otp=str(out)
    otp2=otp[2:6]
    print("Your",i,"otp is",otp2)
