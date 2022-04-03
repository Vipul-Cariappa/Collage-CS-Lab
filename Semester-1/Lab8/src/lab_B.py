# program to compute the number of characters, words and lines in a text file

with open("note.txt") as file:
    line_count = 0
    word_count = 0
    character_count = 0

    line_content = file.readline()
    
    while line_content:
        line_count += 1

        word_count += len(
            line_content.split()
        )

        character_count += len(line_content)
        line_content = file.readline()

print(f"Line Count is {line_count}")
print(f"Word Count is {word_count}")
print(f"Character Count is {character_count}")
