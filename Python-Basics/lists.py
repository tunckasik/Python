# list of the names
names = ["MHT", "MNR", "NSB"]

names.append("ALI")

names.sort()

print(names)

# To know to names class
print(type(names))

# Can have mixed values in the same list
mixedList = ["hello", 10, True, 1.0]
print(mixedList)

# Empty List
emptyList = []
empoList = list()
print(emptyList, empoList)

# Lists can be indexed
listIndex = ["AWS", 1, "Azure", 2.0, "Ally",  True, "Python"]
a = "Pychram"
a_list = list(a)
print(listIndex)
print(a_list)

# Length of the List:
print(len(listIndex))

#'  :  :  ' -> first part start index : second part last index(Not Includes) : consecutiveness
print(listIndex[:6:2])
# output ['AWS', 'Azure', 'Ally']

print(listIndex[::2])
# outout ['AWS', 'Azure', 'Ally', 'Python']

print(listIndex[:7:3])
# output ['AWS', 2.0, 'Python']

print(listIndex[1::3])
# output [1, 'Ally']

# to change the value of the list
listIndex[0]="GCP"
listIndex[3]=3
print(listIndex)

# Changing more than one element in the list
print(listIndex)
listIndex[:3] = ["Bronze", "Java", True]
# That will change first 3 index 0., 1. and 2.
print(listIndex)

# # insert()
# print(list.insert(2,"GOBAC"))

# adding a new element at the end of the list by append()
listIndex.append("Appended")
print(listIndex)

# removing an existing element by remove()
listIndex.remove(1)


# removing an existing element by selecting the index: pop()
listIndex.pop(4)

# removing all by clear()
listIndex.clear()

# sorting
listNum = [15,106,26,56,100]
listNum.sort
print(listNum)

listWord = ["Zebra", "Reff", "A Class"]
print(listWord)

# merging two lists
listMerged = listNum + listWord
print(listMerged)


#nested list
matrix = [[[k for k in range(4)] for j in range(3)] for i in range(2)]
print(matrix[:][:][:])