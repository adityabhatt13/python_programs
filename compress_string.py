s = "abbcccdddd"
compressed = ""
index = 0
while index != len(s):
    count = 1
    while index < len(s)-1 and s[index] == s[index+1]:
        index += 1
        count += 1
    if count == 1:
        compressed += s[index] 
    else:
        compressed += s[index] + str(count)           
    index += 1
print(compressed)         
