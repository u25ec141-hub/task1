#question7
list = [1,1,20,26,28,22,3,20,26]

i = 0

while i < len(list):
    j = i + 1
    while j < len(list):
        if list[i] == list[j]:
            list.remove(list[j])
        else:
            j += 1
    i += 1

print(list)
