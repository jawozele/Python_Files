# Thanks for viewing my Python files
# Here's a 'Find Age App"
# The system prompts the User to enter their DOB
# If the age is less than 18 the system displays the line of code in Line 14.

import datetime

YearOfBirth=input("Enter your year of birth:")
CurrentYear=datetime.datetime.now().year
Age=CurrentYear-int(YearOfBirth)
if(Age>=18):
    print("Your age is {} and you are an Adult".format(Age))
if(Age<18):
    print("Your age is {} and you are not an Adult".format(Age))
print("App is done")