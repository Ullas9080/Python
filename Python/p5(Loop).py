#While = It will excute program untill it become true
'''name=""
while len(name)==0:
    name=input("Enter your name:")
print("Hello",name)
i=0
while i<10:
    print(i)
    i+=1'''
#for loop
n=int(input("Enter the sum number"))
sum=0
count=0
for i in range(0,n-2):
    count=count+1
    print(i)
    sum=sum+i
print(sum)
print(count)   