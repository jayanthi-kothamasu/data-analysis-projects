def make_line(size):
    line = ""
    for i in range(size):
        line += "#"
    return line

def make_square(size):
    square = ""
    for i in range(size):
       square += ((make_line(size)) + "\n")

    return square
    
print(make_square(5)) 


def make_space_line(numSpaces, numChars):
    spaces = " " * numSpaces       # create numSpaces spaces
    hashes = "#" * numChars        # create numChars hashes
    return spaces + hashes + spaces  

print(make_space_line(3,5))
