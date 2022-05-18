a = {1:2,3:"abc","li":[4,"adi"],"dict":{1:2}}
# print(a[1])
# print(a["li"])

# [] FUNCTION GIVES AN ERROR WHEN THE ELEMENT IS NOT IN THE DICT, BUT GET FUNCTION DOESN'T

# print(a.get("li"))

# print(a.get(5,"not present"))

# print(a.keys())
# print(a.values())
# print(a.items())

# for i in a:
#     print(i, a[i])

# for i in a.values():
#     print(i)  

print("li" in a)    
print("abc" in a)  

