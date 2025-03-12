a =int(input("enter the value of a "))
b =int(input("enter the value of b "))
print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
print("Enter 5 for Remainder")
num=int(input())
if num==1 :
 print("Addition: ", a+b)
elif num==2 :
 print("Subtraction: ", a-b)
elif num==3 :
 print("Multiplication: ", a*b)
elif num==4 :
 print("Division: ", a/b)
elif num==5 :
 print("Remainder: ", a%b)
else :
 print("Enter the wrong number")