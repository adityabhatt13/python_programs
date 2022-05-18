s = "This is Aditya"
words = s.split(" ")
newWords = []
for word in words:
    word = word[::-1]
    newWords.append(word)
newSentence = " ".join(newWords)

# print(newSentence)
        
        

        