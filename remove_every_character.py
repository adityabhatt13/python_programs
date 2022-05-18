s = input()
remove = input()

for i in range(len(s)):
    if remove not in s:
        break
else:
    if s[i] == remove:
        new_s = s.replace(remove,"")             
    print(new_s)        
print(s)
