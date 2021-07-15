import numpy as np
l1=([1,2,3,4,5])
n1=np.array(l1)
print(n1)
print(type(n1))
n1=np.zeros((2,4))
print(n1)

#arrange mathod

n2=np.arange(10,20)
print(n2)
#random mathod
n3=np.random.randint(10,20,5)
print(n3)
# numpy shape
n1=np.array([[4,5,6],[3,7,8]])

print(n1)
n1.shape=(3,2)
print(n1)
# vstock ,hstock,column stock

n4=np.array([20,30,40,50])
n5=np.array([60,70,80,90])
print(np.vstack((n4,n5)))
print(np.hstack((n4,n5)))
print(np.column_stack((n4,n5)))
