n = int(input())
found = False
for i in range(2, n):
    print("Inside loop")
    if n%i == 0:
        found = True
        break

if found:
    print("Not prime")
else:
    print("Prime")    