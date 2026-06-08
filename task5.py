#question6
list = [34,65,87,12,36]
largest =list[0]
seclargest =list[0]
for val in list:
    if val>largest:
        seclargest = largest
        largest = val
       
    elif val>seclargest and val!=largest :
        seclargest = val
else:
    print("sec largest value",seclargest)