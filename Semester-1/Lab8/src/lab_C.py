# program to find largest word in a file

def largest_word(filename):
    with open(filename) as file:
        content = file.read()

    words = content.split()
    largest_word = words[0]
    length = len(largest_word)
    
    for i in words:
        if len(i) > length:
            length = len(i)
            largest_word = i

    return largest_word

print(
    largest_word("note.txt")
)
