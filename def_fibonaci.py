def check_fibonacci(n):
	a = 0
	b = 1
	for i in range(0, n+1):
         c = a + b
         a = b
         b = c
         if n == b or n==0 or n==1:
        	 return True
        	 break
	else:
         return False
    
n=int(input())
if check_fibonacci(n):
    print("true")
else:
    print("false")
