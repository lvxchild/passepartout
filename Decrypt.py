from datetime import datetime
import sys

# Variables
txtArr = []
isValid = False;

# Control code to prevent errors
if len(sys.argv) <= 1:
	sys.exit("ERR - You need to specify a file.")
elif len(sys.argv) > 2:
	sys.exit("ERR - You can't decrypt more than one file at once.")
# Get argument and transform it into a string
file = str(sys.argv[1])
file = open(file, "r")
cpdTxt = file.readline().strip()
# Create an array item every four characters
for i in range(0, len(cpdTxt), 4):
	j = i+4
	txtArr.append(cpdTxt[i:j])
# Start decrypting file: for every character firstly it does remove appended and
# prepended junk code, then add '0x' to every array item (not strictly needed but
# still), transform hex code into decimal, subtract 10 and at last print character.
for i in range(len(txtArr)):
	if i % 2 == 0:
		txtArr[i] = txtArr[i][:-2]
	elif i % 2 == 1:
		txtArr[i] = txtArr[i][-2:]
	txtArr[i] = '0x' + txtArr[i]
	print (chr(int(txtArr[i], 16) - 10), end='')
print('')
# Control loop for creating an unencrypted file with text.
while isValid == False:
	choice = input("Do you want to create an unencripted file? (y/n) ")
	choice = choice.lower()
	if choice == 'y':
		while isValid == False:
			choice = input("Do you want to rename the newly created cripted file? (y/n) ")
			choice = choice.lower()
			if choice == 'y' or choice == 'n':
				# Let user choose a name for the file.
				if choice == 'y':
					txtName = input("New name of the file: ")
					isValid = True;
				# Use format DayMonthYearHourMinuteSecond to name the file.
				elif choice == 'n':
					txtName = datetime.now()
					txtName = "unencrypted-" + txtName.strftime("%d%m%Y%H%M%S")
					isValid = True;
				# Append file extension to file name, print on terminal that the
				# file has been created and create the file.
				txtName+=".txt"
				file = open(txtName, "x")
				file.write(cpdTxt)
				print ("New unencrypted file with name " + txtName + " has been created.")
			else:
				print ("The only available choices are 'y' and 'n'.")
	elif choice == 'n':
		isValid = True;
	else:
		print ("The only available choices are 'y' and 'n'.")