import sys

def findUnique(arr, n) :
    visited = []
    for i in range(0,n):
        if arr[i] in visited:
            continue
        
        k = i + 1
        flag = False
        for j in range(k,n):
            if arr[i] == arr[j]:
                flag = True
                visited.append(arr[j])
                break
        if not flag:
            return arr[i]
    return arr[0]           
    

        

def takeInput() :
    n = int(sys.stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    return arr, n



t = int(sys.stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    print(findUnique(arr, n))

    t -= 1