# update,add,remove method

s1={34,"mango","mango",3.4}
print(s1)
s1.add("orange")
print(s1)

s1.update([23,45,67,])
print(s1)

s1.remove(67)
print(s1)
# common and union method
s2={1,2,3,3,4,5,6,}
s3={3,4,5,6,7,6,5,4,3}
print(s2.union(s3))
print(s2.intersection(s3))