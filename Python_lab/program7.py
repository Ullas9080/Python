#Write a pro gram to filter the number 
def even(x):
    return x%2==0
a=[1,2,3,4,5,6,7,8,9,10,12,13,14,15]
result=filter(even,a)
print("Original list : ",a)
print("Filter list :",list(result))