# a = {}
# print(type(a))

a = {1:"the",2:"a","hello":5}
# print(a)
# print(len(a))

# b = a.copy()
# print(b)

c = dict([(1,"the"),(2,"a"),("hello",5)])
# print(c)

d = dict.fromkeys([1,2,"hello"],"the") #SAME VALUES WILL BE PRINTED
print(d)