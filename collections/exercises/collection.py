
#revenues = [2300,1800,2100,2500,1950,2750,3000,596,1111]

expenses =[106,400,333,150,240,370]
for expense in expenses:
    print(f"expense after tax: ${expense * 1.08:.2f}")


for i in range(len(expenses)):
    print(f"expense number{i}:original expense{expenses[i]}")

employee = ("ID-14","alex chen","Data analyst")
print(employee[1])
employee_as_list = list[employee]
employee[1] = "alex young"
print(employee)