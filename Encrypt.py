from random import SystemRandom
from secrets import SystemRandom
from datetime import datetime

# Variables
cpdTxt = ""
txt = input ("Insert text to encrypt: ")
txtArr = []
isValid = False;

#Cycle every character.
for i in range(len(txt)):
	# Create a new array item containing the character,
	# turn it into ASCII and ad 10 to the number then turn it into an hex value.  
	txtArr.append(txt[i])
	txtArr[i] = ord(txtArr[i]) + 10
	txtArr[i] = hex(txtArr[i])
	# If-else statement that add junk code to every array item swapping between.
	# if == 0 append hex junk to item | if == 1 prepend hex junk to item
	if i % 2 == 0:
		txtArr[i] = txtArr[i] + str(hex((SystemRandom().randrange(16,255))))
	elif i % 2 == 1:
		txtArr[i] = str(hex((SystemRandom().randrange(16,255)))) + txtArr[i]
	# Remove '0x' on every hex code then create a string containing everything.
	txtArr[i] = txtArr[i].replace('0x', '')
	cpdTxt += txtArr[i]
# Simple control loop that let the use choose if they want to give a name
# to the newly created file of let the script do it.
# If choice = n the file name will contain DayMonthYearHourMinuteSecond.
# If a wrong character is use an warning will appear.
while isValid == False:
	choice = input("Do you want to rename the newly created cripted file? (y/n) ")
	choice = choice.lower()
	if choice == 'y':
		txtName = input("New name of the file: ")
		isValid = True;
	elif choice == 'n':
		txtName = datetime.now()
		txtName = "encripted-" + txtName.strftime("%d%m%Y%H%M%S")
		isValid = True;
	else:
		print ("The only available choices are 'y' and 'n'.")
# Append extension to the created file, print that the file has been created
# successfully and finally create a new file a write the crypted text inside.
txtName+=".txt"
file = open(txtName, "x")
file.write(cpdTxt)
print ("New encrypted file with name " + txtName + " has been created.")