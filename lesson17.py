from Tack1 import with_index
from Tack2 import in_range
from Tack3 import Iterator
#Tack1(enumerate)
a = [10,20,30,40]
# for i in with_index(a):
#     print(i)
print(list(with_index(a,0)))
#Tack2(range)
print(in_range(0,6,3))
print(in_range(-3,6))
#Tack3(iter)
b = Iterator('[5,4,3,2,1]')
for i in b:
    print(i)