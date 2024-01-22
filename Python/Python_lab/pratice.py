#program1
'''a=10
b="Ullas"
c=12.09
d=12.j
e=True
print(f"Data type of {a} : {type(a)}")
print(f"Data type of {b} : {type(b)}")
print(f"Data type of {c} : {type(c)}")
print(f"Data type of {d} : {type(d)}")
print(f"Data type of {e} : {type(e)}")'''

'''#Program2
list=[12,34,56,78,90]
#insert
list.insert(3,"Hello")
print(list)
#append
list.append("Python")
print(list)
#remove
list.remove(90)
print(list)
#pop
list.pop()
print(list)
#clear
list.clear()
print(list)'''

#program3
'''tuplenumber=(12,34,56,78,90)
print(tuplenumber)
tuplenames=("One","Two","Three","Four","Five","Six")
print(tuplenames)
addtuple=tuplenames+tuplenumber
print(addtuple)
print(len(addtuple))
print(addtuple[0:7])
print(addtuple[3:5])'''

#program4
'''student={1:"Ullas",2:"Nihar",3:"Prashid",4:"Muthuraj"}
print(student)
print(student[3])
print(student.get(4))
x=student[1]="Ullas gowda"
print(x)
print(len(student))'''

#program5
'''def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print("1.Addition")
print("2.Subtraction")
print("3.Multiplucation")
print("4.Division")

choice=int(input("Enter your choice\n"))
a=int(input("Enter first number\n"))
b=int(input("Enter second number\n"))
if choice==1:
    print("Addtion two number is :",add(a,b))
elif choice==2:
    print("subtraction two number is :",sub(a,b))
elif choice==3:
    print("Multiplication of two number is :",mul(a,b))
elif choice==4:
    print("Division of two number is :",div(a,b))
else:
    print("Invalid choice")'''

#program6
'''number=int(input("Enter the number\n"))
if number>0:
    print(f"{number} is a positive number")
else:
    print(f"{number} is a negative number")'''

#program7
'''def even(x):
    return x%2==0
a=[1,2,3,4,5,6,7,8,9,10,12,13,14,15]
print(f"Unfilter list {a}")
f=filter(even,a)
print("filter :",list(f))'''

#program8
'''import datetime 
time=datetime.datetime.today()
date=datetime.datetime.now()
print(time)
print(date)'''

#program9
'''from datetime import date
from datetime import timedelta
import datetime
presentdate=date.today()
print("Present Date")
print(presentdate)
enddate=presentdate+timedelta(days=10)
print("EndDate")
print(enddate)'''

#progarm11
'''file=open("program11.txt","r")
read=file.read()
count=read.count("e")
print("Freqency of ",count)'''

#program12
'''import numpy as np
arr=np.array([[4,5,6,7],[2,3,4,5]])
print(type(arr))
print(arr.ndim)
print(arr.shape)
print(arr.dtype)'''

#program13
'''import pandas 
dataframe1=pandas.DataFrame({"Id":[101,102,103,104],"Name":["Ullas","Nihar","Abhi","Prashid"]})
print(dataframe1)
print()
dataframe2=pandas.DataFrame({"Id":[201,102,203,204],"Name":["Srikrant","Sanjana","Thilak","Mutu"]})
print(dataframe2)
print()
frame=[dataframe1,dataframe2]
print(frame)
print()
concat=pandas.concat(frame)
print(concat)'''

#program15
'''import math
radius=int(input("Enter the radius :"))
area=math.pi*radius*radius
print(area)
circumference=math.pi*radius*2
print(circumference)'''




























