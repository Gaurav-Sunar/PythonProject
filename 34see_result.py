result = {
    '00411AN' : '4',
    '332AGGE' : '2',
    '3454GDG' : "3",

}

symbol_no = input("Enter your symbol number: ")

result = ""
for i in resultset.keys():
    if symbol_no == i:
        result = resultset[i]
        break
    else:
        result = ''

    if result != "":

print(f"Your Result is {result}")
else:
   print(f"Your Symbol no not found.") 