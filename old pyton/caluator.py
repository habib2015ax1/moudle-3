def add(a,b):
    print (a+b)
def sub(a,b):
    print(a-b)
def multiply(a,b):
    print(a*b)
def divide(a,b):
    print(a/b)
print("input your choice")
print("1.addion 2.subtraction 3.multiply 4.divide")
number1=int(input("enter a number"))
number2=int(input("enter a number"))
choice=input("enter your choice")
if choice=="1":
 add(number1,number2)
elif choice=="2":
     sub(number1,number2)
elif choice=="3":
 multiply(number1,number2)
elif choice=="4":
   divide(number1,number2)