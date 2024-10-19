def validatePostcode(postcode):
    
    postcode = postcode.upper().replace(' ', '')
    
    if len(postcode) < 5 or len(postcode) > 7:
        return False
    
    def is_letter(char):
        return 'A' <= char <= 'Z'
    
    def is_digit(char):
        return '0' <= char <= '9'
    
    start = postcode[:-3]
    end = postcode[-3:] 
    
    if not (is_digit(end[0]) and is_letter(end[1]) and is_letter(end[2])):
        return False
    
    return is_letter(start[0]) and is_letter(start[1]) and is_digit(start[2]) and is_letter(start[3])

postcode = input('Please enter a postcode: ')
if validatePostcode(postcode):
    print(f'{postcode} is a valid postcode.')
else:
    print(f'{postcode} is not a valid postcode.')