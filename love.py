import random

name ="Pubudhi"
result = ''

print(name[0])
print(name[-1])
print(len(name))

# for loop in python

for i in range(len(name)):
	if i % 2 == 0:
		print(name[i])
		result = result + name[i]
		print('result just changed to :' + result)

print(str(5) + '5')

print(int('5'))

print(input('What is your pet name?'))
pet = input('What is your pet name?')

print(pet)

#how to generate random number in python??
for i in range(10):
	print(random.randint(10,20))

# 00x00xxx
# 0x0xx000
# 0x0x000x















	