def sumUnique(li):
    s = set()
    for i in li:
        s.add(i)
    sum = 0
    for i in s:
        sum += i
    print(sum)

sumUnique([1,2,4,1,5,3,1,2,4,3,1,2,3,4,5,1,2,3,4,1,3,2,1,5])