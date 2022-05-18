# s = input("string: ")
# char1 = input("Character to be replaced in the string: ")
# char2 = input("Replace with: ")
# s = s.replace(char1,char2)
# print("New string is:",s)

def replace(str,char1,char2):
    newStr = ""
    for char in str:
        if char == char1:
            newStr += char2
        else:
            newStr += char
    return newStr            
str = "asasasasasasa"
str = replace(str,"s","d")
print(str)