a = {"adi","abc",12,1,"bye",121}

# print(12 in a)
# print("add" in a)

# for v in a:
#     print(v) # NO ORDER

# print(len(a))

a.add("temp")
# print(a)

b = {"adi",1,2,"good"}
a.update(b)
# print(a)

a.remove("temp")
# print(a)

# REMOVE GIVES AN ERROR WHEN ELEMENT IS NOT IN THE SET BUT DISCARD DOESN'T GIVE AN ERROR

a.discard(121)
# print(a)
a.discard("add")
# print(a)

print(a.pop()) # RANDOM ELEMENT GETS REMOVED
print(a)