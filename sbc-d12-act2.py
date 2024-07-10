sentence = "The qick brown fox jumps over the lazy dog"
words = []
split_words = ""

for char in sentence:
    if char != " ": 
       split_words += char  
    else:
        if split_words:  
            words.append(split_words)  
            split_words= "" 

if split_words:
    words.append(split_words)  

print(words)
