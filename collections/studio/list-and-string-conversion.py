proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]



# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces. 
for i in strings:
    print(i)


# # b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string. if ','in strings:
if "," in proto_list1:
    split_list = proto_list1.split(",")
    split_list.reverse()
    new_proto_list1 = ",".join(split_list)
    print(new_proto_list1)




# c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
if ";" in proto_list2:
    split_list = proto_list2.split(";")
    split_list.sort()

    new_proto_list2 = ";".join(split_list)
    print(new_proto_list2)



# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.
if " " in proto_list3:
    split_list = proto_list3.split(" ")
    split_list.sort()
    split_list.reverse()
    new_proto_list3 = " ".join(split_list)
    print(new_proto_list3)



# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
if ", " in proto_list4:
    split_list = proto_list4.split(" ")
    split_list.reverse()
    separator = " "
    new_proto_list4 = separator.join(split_list)
    print(new_proto_list4)
