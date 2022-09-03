mylist = []
counter = 0
while counter < 5:
    number = int(input("please enter a number: "))
    mylist.append(number)
    counter = counter + 1
sortedlist = mylist.sort()
print(mylist[-1])