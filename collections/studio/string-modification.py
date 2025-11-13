my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.

modified_word = my_string[3:]+ my_string[ :3]
print(modified_word)


# Use a template literal to print the original and modified string in a descriptive phrase.

modified_string = my_string[3: ]+ my_string[ :3]
print(f"the original string '{my_string}' and modified string is '{modified_string}' ")

# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.

Num_of_letters = int(input("Enter the num of letters that will be relocaated "))
modified_Word = my_string[Num_of_letters: ]+ my_string[ : Num_of_letters]
print(f" the original word is '{my_string}' after moving '{Num_of_letters}' letters to the end.It becomes '{modified_Word}' ")


# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.

Num_Of_Letters = int(input("Enter the num of letters to move from start to end"))
if  Num_Of_Letters > len(my_string):
    print('you entered input is longer than the original string')
    Num_Of_Letters = 3
    modified_string = my_string[Num_Of_Letters:]+my_string[:Num_Of_Letters]
    print(f"you entered longer word so it moved to default 3 numbers,now the modified word is '{modified_string}' ")
else:
     modified_string = my_string[Num_Of_Letters:]+my_string[:Num_Of_Letters] 
     print (f"the modified string  is '{modified_string}' ")