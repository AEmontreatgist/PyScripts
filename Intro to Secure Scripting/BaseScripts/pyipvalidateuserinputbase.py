import pyinputplus as pyip

# Prompt the user to enter a number between 1 and 10
number = pyip.inputInt("Please enter a number between 1 and 10: ", min=1, max=10)

# Prompt the user to enter an email address
email = pyip.inputEmail("Please enter your email address: ")

# Prompt the user to enter a password with specific criteria
password = pyip.inputPassword("Please enter a password with at least one uppercase letter, one lowercase letter, 
and one digit: ", 
                              minlen=8, uppercase=True, lowercase=True, digits=True)

# Print the validated inputs
print("Validated inputs:")
print(f"Number: {number}")
print(f"Email: {email}")
print(f"Password: {password}")

#To validate a floating-point number: use inputFloat instead of inputInt.
#To validate a date in YYYY-MM-DD format: use inputDate with the format parameter set to "YYYY-MM-DD".
#To validate a yes/no answer: use inputYesNo.
#To validate a phone number: use inputPhone.
