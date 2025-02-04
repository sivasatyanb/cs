website = 'www.rgshw.com'
string = ''
flag = False
for letter in website:
    if letter == '.':
        flag = True
    elif flag and len(string) < 3:
        string += letter.upper()
position = 0
for letter in string:
    position += ord(letter)
print(position)