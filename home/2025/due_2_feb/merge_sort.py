list1 = ["banana", "grape", "melon", "pear"]
list2 = ["apple", "pear", "pineapple", "raspberry"]
list3 = []
list1Head = 0
list2Head = 0

while list1Head != len(list1) and list2Head != len(list2):
    item1 = list1[list1Head]
    item2 = list2[list2Head]
    if item1 < item2:
        list3.append(item1)
        list1Head += 1
    elif item2 < item1:
        list3.append(item2)
        list2Head += 1
    elif item1 == item2:
        list3.append(item1)
        list3.append(item2)
        list1Head += 1
        list2Head += 1
    print(list3)