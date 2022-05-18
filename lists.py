li = [1, 2, 3]
print(li) 

print(type(li)) #type

li.append("aditya") #adds object to the end of list
li.extend("bhatt") #adds every element in the object to the end of list

print(li[4]) #to access a specific index 
print(li[3:9]) #to access the list from a specific index to a specific index 
li.insert(3,4) #inserts object at specific index
li.insert(10, "Good")
li.insert(4,[5,6,7,8]) #inserting a list in a list at index 4
print(li)

li.remove("Good")
li.append(3)
li.pop() #obj at last index is removed
print(li.pop(3)) #obj at index 3 is removed
print(li)
