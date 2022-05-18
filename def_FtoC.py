def printTable(start,end,step):
    while start<=end:
        f = start
        c = ((f-32)*(5/9))
        print(start, end="    ")
        print(int(c))
        start += step

	   
s = int(input())
e = int(input())
step = int(input())
printTable(s,e,step)





