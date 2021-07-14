import pandas as pd
s1=pd.Series([2,3,4,3])
print(s1)


s1=pd.Series([2,3,4,5],index=['a','b','c','d'])
print(s1)
#pandas with dict
s1=pd.Series({'a':20,'b':40,'c':10})
print(s1)
#pandas with dict and index
s1=pd.Series({'a':20,'b':40,'c':10},index=('a','b','d','c'))
print(s1)

#pandas index
s1=pd.Series([2,3,4,3,5,6,7,8,9])
print(s1[3])
print(s1[-3:])


#adding
s1=pd.Series([2,3,4,3,5,6,7,8,9])
print(s1+5)

#adding two series
s1=pd.Series([2,3,4,3,5,6,7,8,9])
s2=pd.Series([20,30,40,30,50,60,70,80,90])
print(s1+s2)



