#single level inhertance
'''class Fruits:
    def apple(self):
        print("Eat a apple daily ,keep a Doctor away")

    def pineapple(self):
        print("pineapple is not equal to apple")

class childFruits(Fruits):
    pass

child=childFruits()
child.apple()
child.pineapple()'''

#multilevel
'''class Math:
    def add(self,num1,num2):
           sum=num1+num2  
           print(f"Addition of two number is {sum}")
           return  sum     

    def sub(self,num1,num2):
        sum=num1-num2
        print(f"Subtraction of two number is {sum}")
        return sum

    def mul(self,num1,num2):
        sum=num1*num2
        print(f"Multiplication of two number is {sum}")
        return sum
       

    def div(self,num1,num2):
        sum=num1/num2
        print(f"Division of two number is {sum}") 

        return sum
        

class Add(Math):
    pass

class Sub(Math):
    pass

class Mul(Math):
     pass

class Div(Math):
     pass
add=Add()
sub=Sub()
mul=Mul()
div=Div()

print(f"1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")
choice=int(input("Enter your Choice :"))
num1=int(input("Enter the first value :"))
num2=int(input("Enter the Second value :"))
if choice==1:
     add.add(num1,num2)
elif choice==2:
     sub.sub(num1,num2)
elif choice==3:
     mul.mul(num1,num2)
elif choice==4:
     div.div(num1,num2)'''
#Multiple Inhertance
'''class University:
    def Bms(self):
        print("I am back to Bms")
class University1:
    def Dayanandh(self):
        print("I will never take admission in Dayanandh")
class College(University,University1):
    pass
college=College()
college.Bms()
college.Dayanandh()'''
