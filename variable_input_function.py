def sum_multi(a,b, *tuple):
    sum = a + b
    multi = a*b
    for i in tuple:
        sum = sum + i
        multi *= i
    return sum,multi

print(sum_multi(1,2,3,4))


