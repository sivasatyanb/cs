string = input()
# part a
list1 = []
for letter in string:
    ascii = ord(letter)
    list1.append(ascii)
print(list1)
# part b
# convert each ascii value to hex
list2 = []
for ascii in list1:
    hex_val = hex(ascii)
    list2.append(hex_val)
print(list2)
# part c
# convert each hex value to binary
list3 = []
for hex_val in list2:
    binary_val = bin(int(hex_val, 16))
    list3.append(binary_val)
print(list3)