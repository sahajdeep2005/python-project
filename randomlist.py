import random
num = int(input("Enter number of element "))
stop= int(input("Enter the last number "))
list=[]
i=1
while i<=num:
    n=random.randrange(i,stop)
    if n % 2==1:
     i=i+1
     if n not in list:
      list.append(n)

list.sort()
print("This is number list")
print(list)
