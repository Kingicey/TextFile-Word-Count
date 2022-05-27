# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content():
    text = open("story.txt", "r")
    read_text = text.read()

    text.close()
    
    return read_text

check = read_file_content()
print(check)
def count_words():
    # text = read_file_content("./story.txt")
    # text = read_file_content("story.txt")
    text = read_file_content()
    for char in "-.,?\n":
        text = text.replace(char, ' ')
    words = text.lower()
    words = words.strip()
    doc = {}
    splitted_word = words.split()

    for word in splitted_word:
        if word in doc:
            doc[word] += 1
        else:
            doc[word] = 1
    print(doc)


    # return {"as": 10, "would": 20}
count_words()

