import random

a = random.randint(1,6)

temp = 1
print(a)

while temp <= a :

    if(temp%2==0):

        print("0" , end="")
        temp = temp+1
    else:
            print("\n" + "0", end="")
            temp=temp+1
    
    
    
