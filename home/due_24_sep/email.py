# function to generate email based on user details
def generateEmail(fileName, yearOfEntry, forename, surname):
    email = yearOfEntry[-2:] + surname[:4] + forename[:3] + '@rgshw.com'
    writeToFile(fileName, email)
    return email

# procedure to write to files    
def writeToFile(fileName, email):
    with open(fileName, 'a') as f:
        f.write(email + '\n')
        f.close()

# get user inputs and pass into function when called        
yearOfEntry = int(input('Please enter the year you joined RGS: '))
forename = str(input('Please enter your first name: '))
surname = str(input('Please enter your last name: '))
fileName = 'data.txt'
email = generateEmail(fileName, yearOfEntry, forename, surname)

# output result
print('Your email is:', email)