# This is a program to convert
# from the old currency: pounds/shillings/pennies
# to the new currency: pounds/pence (or vice versa)

# find out whether to convert from new currency to old currency
# (or vice versa)
year = int(input('What year are we in?: '))
new = False
old = False

if year > 1970:
    new = True
else:
    old = True

# logic to convert from new to old
if new:
    x = float(input('Please enter the new currency to convert in pounds: '))
    
    # formula: old pennies = new pounds * 240
    pennies = x * 240
    pounds = 0
    shillings = 0
    
    # find number of old pounds and shillings
    while pennies > 240:
        pennies -= 240
        pounds += 1
    while pennies > 12:
        pennies -= 12
        shillings += 1
    
    # output result
    print(f'£{x} in the new currency converts to {pounds} pounds, {shillings} shillings and {int(round(pennies, 0))} pennies in the old currency!')

# logic to convert from old to new
if old:
    
    # input old currency
    pounds = int(input('Please enter the number of old pounds: '))
    shillings = int(input('Please enter the number of old shillings: '))
    orig_pennies = int(input('Please enter the number of old pounds: '))
    
    # make all of the old currency into pennies
    pennies = orig_pennies
    pennies += pounds*240
    pennies += shillings*12
    
    # convert to new currency (in pounds) and round to 2 d.p. for pence
    gbp = pennies / 240
    pence = '00'
    gbp = round(gbp, 2)
    
    # extract the pence from gbp
    pence = str(gbp)[-2:]

    # output results
    print(f'The new currency equivalent of {pounds} pounds, {shillings} shillings and {orig_pennies} pennies is £{int(round(gbp, 0))}.{pence}!')