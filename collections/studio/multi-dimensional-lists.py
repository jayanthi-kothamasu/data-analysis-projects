food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
cabinet_list1 = food.split(",")
cabinet_list1.sort()
cabinet_list2 = equipment.split(",")
cabinet_list2.sort()
cabinet_list3 = pets.split(",")
cabinet_list3.sort()
cabinet_list4 = sleep_aids.split(",")
cabinet_list4.sort()



# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = [cabinet_list1, cabinet_list2, cabinet_list3, cabinet_list4]
print(cargo_hold)


# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
choice = int(input("Select a cabinet(0-3)in the cargo hold list " ))
print("you selected choice is ", choice)
print(cargo_hold[choice])

# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.
choice = int(input("select a cabinet(0-3) "))
if 0<= int(choice)<=3:
    choice= int(choice)
    print("Cabinet {} contains: {}".format(choice, cargo_hold[choice]) )
else:
    print("Error,Invalid cabinet number")    



# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”

cabinet_choice = int(input("select a cabinet (0-3) "))
if 0 <= int(choice) <= 3:
    choice = int(choice)
    item_choice = input("enter an item to search for ").lower
    if item_choice in cargo_hold[cabinet_choice]:
     print(" cabinet{}contains{} " .format (cabinet_choice,item_choice))
    else:
        print("cabinet {} does not contain {}" .format (cabinet_choice,item_choice))
else:
   print("Error, Invalid number")           
