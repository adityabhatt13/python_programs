n = input()
total = 0
even = 0
for c in n:
    c = int(c)
    total += c
    if c%2 == 0:
        even += c
odd = total - even
print(even, odd)        