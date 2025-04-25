number=[1,2,3,4,5]
def double (number):
    return number*2
result=map(double,number)
print(list(result))


#filter.py
number=[1,2,3,4,5]
    
result=filter(lambda n:n %2==0,number)
print(list(result))



#reduce.ppp
from functools import reduce
expences=[
   (' school fee',45680),
   ('house rent',20000),
   ('food',1500),
    ('transport',2000)
] 

total = reduce(lambda a, b: a + b[1], expences, 0)
print(total)