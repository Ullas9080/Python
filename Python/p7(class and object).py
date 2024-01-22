class Car:
    def add(self,num1,num2):
        sum=num1+num2
        print(f"addition of two number is {sum}")
        return sum

    def __init__(self,brand,model,cc):
        self.b=brand
        self.m=model
        self.c=cc
        print(f"Brand={self.b}\nModel={self.m}\nCC={self.c}")

carbrand=input("Enter car Brand :")
carmodel=input("Enter car Model :")
carcc=input("Enter car cc :")
car=Car(carbrand,carmodel,carcc)

value1=input("Enter value1 :")
value2=input("Enter value2 :")
car.add(value1,value2)

