import re

password = str(raw_input('Enter your password: '))

passRegex = re.compile(r'''(
	(?=.*[A-Z].*)
	(?=.*[a-z].*)
	(?=.*[0-9].*)
	(?=.*[*&#$!@].*)
	.{8,})''', re.VERBOSE)

try:
	if password == str(passRegex.findall(password)[0]):
		print('Strong password')
	else:
		print('Weak password')
except:
	print('Weak password')
