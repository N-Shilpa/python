def bigger(num1,num2,num3):

    if(num1>num2) and (num1>num3):
        return("num1 is bigger")
    elif(num2>num1) and (num2>num3):
        return("num2 is bigger")
    else:
        return("num3 is bigger")
num1=int(input("enter first number"))
num2=int(input("enter second number"))
num3=int(input("enter third number"))
print(bigger(num1,num2,num3))