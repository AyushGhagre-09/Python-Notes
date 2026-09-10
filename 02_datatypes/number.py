import math
import random
from decimal import Decimal
from fractions import Fraction
print(40+2.23)
print(40+int(2.23))

print("chai"+"code")

str="Hello\nWorld"

print(str)
print(repr(str))

print(math.floor(3.5))
print(math.floor(-3.5))

print(math.trunc(2.8))
print(math.trunc(-2.8))

print(int('10000',2))


print(random.random())
print(random.randint(1,10))

l1 = ['lemon', 'masala', 'ginger', 'mint']
print(random.choice(l1))

random.shuffle(l1)
print(l1)

print((0.1+0.1+0.1)-0.3)

print(Decimal(0.1)+Decimal(0.1)+Decimal(0.1)-Decimal(0.3))
# print(0.3-(0.1+0.1+0.1))

myFra=Fraction(2,7)
print(myFra)


setone={1,2,3,4,5}
print(setone&{1,3}) #intersection
print(setone|{1,3,7}) #union
print(setone-{1,2}) #difference
print(setone^{1,2,3}) # symmentic difference
setone.discard(11)
# add(), return none 
# update(), return none
# remove(),return none it will give error
# discard(), return none it will not give error
# pop(),  return value 
# clear(), return none
# copy(),  return set
# union(), return set
# intersection(), return set 
# difference(), return set
# symmetric_difference() return set
# issuperset(),issubset() return boolean
A = {1, 2}
B = {1, 2, 3, 4}
A.issubset(B)    # True
B.issuperset(A) # True

# boolean
print(True==1)
print(False==0)
print(True is 1)


# Check built-in types(isinstance)
print(isinstance("Hello", str))   # Returns True
print(isinstance(42, int))        # Returns True
print(isinstance([1, 2], dict))    # Returns False


