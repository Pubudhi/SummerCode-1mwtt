# Make a function that returns n number of 'moo's

# Functions, parameters
def moo(n):
	# print('moo' * n)
	return 'moo' * n

# for i in range(4):
# 	moo(i)

# moo(0)
# moo(1)
# moo(4)

def ask_recursively(question):
	print(question)
	reply = input('>').lower()
	if reply == 'yes':
		return True
	if reply == 'no':
		return False
	else:
		print('Please response "yes" or "" no !!!')
		ask_recursively(question)

ask_recursively('Do you wet the bed?')


# Testing 


# Reading and writing files

filename = "alice_in_wonderland.txt"
file = open(filename, "r")
# for line in file:
# 	print(line)

raw = file.read()
print(raw[:80])

print(raw[0:65])
print(raw[65:500])

print('length' +str(len(raw)))

#  calculate a table for each letter in the alphabet from a-z, and count how many times each letter appears in Alice in Wonderland.
# freequency distribution
# a:1545..
# b:462..