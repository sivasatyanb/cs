from email_validator import validate_email, EmailNotValidError

def check_email(email):
    
	try:
		v = validate_email(email)
		email = v['email'] 
		print('This email is valid')
  
	except EmailNotValidError as e:
		print(str(e))

email = input('Please enter your email: ')
check_email(email)