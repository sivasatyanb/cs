# # The easy way:

# from email_validator import validate_email, EmailNotValidError

# def check_email(email):
    
# 	try:
# 		v = validate_email(email)
# 		email = v['email'] 
# 		print('This email is valid')
  
# 	except EmailNotValidError as e:
# 		print(str(e))

# email = input('Please enter your email: ')
# check_email(email)

# The hard but proper way:

# initialising function and taking in required parameters
def check_email(email):
    validity = ''
    breakpoint = False
    
    # this is validation for rule for listed a the bottom of this code
    if not (ord(email[0]) >= 65 and ord(email[0]) <= 90) and not (ord(email[0]) >= 97 and ord(email[0]) <= 122):
        validity = 'Your email does not begin with a letter. It is invalid.'
    
    # iterating through the email address to check for rules 1 and 2
    for i in range(len(email)):
        char = email[i]
        if char == '@':
            if not (ord(email[i-1]) >= 65 and ord(email[i-1]) <= 90) and not (ord(email[i-1]) >= 97 and ord(email[i-1]) <= 122) and not (ord(email[i-1]) >= 48 and (ord(email[i-1])) <= 57):  
                validity = 'Your email does not contain alpha-numeric text before the @ sign. It is invalid.'
            if not (ord(email[i+1]) >= 65 and ord(email[i+1]) <= 90) and not (ord(email[i+1]) >= 97 and ord(email[i+1]) <= 122) and not (ord(email[i+1]) >= 48 and (ord(email[i+1])) <= 57):
                validity = 'Your email does not contain alpha-numeric text after the @ sign. It is invalid.'
            
            for j in range(i, len(email)):
                if email[j] == '.':
                    breakpoint = True
    
    # this is for rule 3
    if not breakpoint:
        validity = 'There is no breakpoint (.) after the @ sign. It is invalid.'
	
	# if the validity is not flagged above, it is set as valid
    if validity == '':
        validity = 'Your email is valid.'
		
    return validity
    
# get inputs from user and output function's return value
email = input('Please enter your email: ')
validity = check_email(email)
print(validity)

# Travi's rules:

# 1) Must have some alpha numeric text before the @sign // done
# 2) Must have some alpha numeric text after the @sign // done
# 3) Must have a . after the @sign and text displayed // done
# 4) cannot start with digits // done