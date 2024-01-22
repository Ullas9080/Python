#Write a program to create a menu with following option
#Additon , subtraction , multiplication , division
def add(n1,n2):
    sum=n1+n2
    print(f"Addition of {n1} and {n2} is {sum}" )
    return sum
def sub(n1,n2):
    sum=n1-n2
    print(f"Subtraction of {n1} and {n2} is {sum}" )
    return sum
def mul(n1,n2):
    sum=n1*n2
    print(f"Multiplication of {n1} and {n2} is {sum}" )
    return sum
def div(n1,n2):
    sum=n1/n2
    print(f"Division of {n1} and {n2} is {sum}" )
    return sum
print("Welcome to Arthmetic program")

x=input("Enter the first number\n")
y=input("Enetr the second number\n")
print("1.To Perform Addition")
print("2.To Perform Subtraction")
print("3.To Perform Multiplication")
print("4.To Perform Division")
print("0.Exits")
choice=int(input("Enter your choice"))

if choice==1:
        print(add(x,y))
elif choice==2:
        print(sub(x,y))
elif choice==3:
        print(mul(x,y))
elif choice==4:
        print(div(x,y))
elif choice==0:
        print("Exits")
else:
        print("Invalid option")