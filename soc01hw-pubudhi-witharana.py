# A few things to try

# *** 01
# Full name greeting. Write a program that asks for a person’s first name, then middle, and then last. Finally, it should greet the person using their full name.

response = ''
fullName = ''

response = input('What is your first name : ')
fullName = response

response = input('What is your middle name : ')
fullName = fullName + ' ' + response

response = input('What is your first name : ')
fullName = fullName + ' ' + response

print('Hello ' + fullName + ', Have a nice day...!')

# *** 02
# Bigger, better favorite number. Write a program that asks for a person’s favorite number. Have your program add 1 to the number, and then suggest the result as a bigger and better favorite number. (Do be tactful about it, though.)
# In here I assume all numbers greater than 50 consider as larger(big) numbers.

Number = input('Hello, What is your favourite number?')
favNumber = int(Number) + 1

if favNumber < 50:
	print('Yeah, It\'s a better number')
else:
	print('OMG! It\'s a big number')

# *** 03
# Angry boss. Write an angry boss program that rudely asks what you want. Whatever you answer, the angry boss should yell it back to you and then fire you. For example, if you type in I want a raise, it should yell back like this:

yourNeed = input('What do you ask from the boss?')
print('WHADDAYA MEAN "' + yourNeed.upper() + '"?!? YOU\'RE FIRED !! ' )