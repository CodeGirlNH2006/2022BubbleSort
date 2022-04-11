import random as rand

def displayList():
    output = "["
    for num in list:
        output += str(num) + ", "
    print(str(output) + "]")
# swap indices 1 and 2
def swap(i1, i2):
    x = list[i2]
    list[i2] = list[i1]
    list[i1] = x

def bubbleSort():
    for x in range(len(list)-1):
        for item in range(len(list)-1):
            if list[item] > list[item+1]:
                swap(item, item+1)
list = []
for x in range(100):
    list.append(int(rand.random()*1000))
displayList()
bubbleSort()
displayList()