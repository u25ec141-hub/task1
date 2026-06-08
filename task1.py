#QUESTION 1 AND 2
list1 =[1,22,28,34,54,23,90,56,78,98,99,45,100,47,33,56,43,44,77,10]
#sum
sum=0
print("SUM OF ALL ELEMENT OF LIST1")
for value in list1:
    sum =sum +value
else:
    print(sum)
print("\n")


#average
print('AVERAGE OF LIST1')
for value in list1:
    sum =sum +value
else:
    print(sum/len(list1))
print("\n")


#max
print('MAXIMUM FROM LIST1')
max = list1[0]
for value in list1:
    if max<value :
        max = value
    else:
        max = max
else:
    print(max)
print("\n")


#min
print('MININUM FROM LIST1')
min = list1[0]
for value in list1:
    if min >value :
        min = value
    else:
        min = min
else:
    print(min)
print("\n")


#print all even number
print('EVEN NUMBERS OF LIST1')

for val in list1:
    if val %2==0:
        print(val)
else:
    print('END')
print("\n")


#print all odd
print('ODD NUMBERS OF LIST1')
for val in list1:
    if val %2!=0:
        print(val)
else:
    print('END')
print("\n")




