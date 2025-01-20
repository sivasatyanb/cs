# function to generate email based on user details
def generateUsername(yearOfEntry, forename, surname):
    email = str(yearOfEntry)[-2:] + surname[:4] + forename[:3]
    return email

# get user inputs and pass into function when called        
yearOfEntry = int(input('Please enter the year you joined RGS: '))
forename = str(input('Please enter your first name: '))
surname = str(input('Please enter your last name: '))
email = generateUsername(yearOfEntry, forename, surname)

# output result
print('Your email is:', email)