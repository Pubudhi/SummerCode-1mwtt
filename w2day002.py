# Week 02 Day 2
# Homework 1 

def asciiAlphabet():
	for i in range(65, 65+26):
		print(i, " stands for ", chr(i))
	for i in range(97, 123):
		print(i, " stands for ", chr(i))

# asciiAlphabet()

# Homework 2

def createCypher(plain):
	cypherText = ""
	for i in range( 0 , len(plain)):
		cypherText = cypherText + str(ord(plain[i]))
	return cypherText

plainText = input("Plain Text > ")
print("Cypher Text > ", createCypher(plainText))

# Homework 3 caeser cypher - get user input as shifting number

shiftingVal = input("Cypher Shifting Value > ")
palinTxt = input("Plain Text > ")
 
def caeserCypher(shiftingValue, palin):
	cyphertxt = ""
	for i in range(0, len(palin)):
		cyphertxt = cyphertxt + str(ord(palin[i]) + int(shiftingValue))
	return cyphertxt

print(" Caeser Cypher Text > ", caeserCypher(shiftingVal, palinTxt))



# ========================

a = "Hello"
b = "World"
c = "Python"
students = [a, b, c]
print(students[0], students[1], students[2])

sisters = ["Molly" , "Loura" , "Katherine", "Mary"]

print(sisters)

members  = [students , sisters]

print(members)

print(members[1][3])

# continent counter
M = 'land'
o = 'water'

world = [
			[o,o,o,o,o,o,o,o,o,o,o],
			[o,o,o,o,o,o,o,o,o,o,o],
			[o,o,o,o,o,o,o,o,o,o,o],
			[o,o,o,o,o,o,o,o,o,o,o],

			[o,o,o,o,o,o,o,o,o,o,o],
			[o,o,o,o,M,M,M,M,M,M,o],
			[o,o,o,o,o,M,M,o,o,o,o],
			[o,o,o,o,o,M,o,o,o,o,o],

			[o,o,o,o,M,M,M,o,o,o,o],
			[o,o,o,o,o,o,o,o,o,o,o],
			[o,o,o,o,o,o,o,o,o,o,o],

		]
def continent_counter(world, x, y):
		if world[y][x] != 'land':
			return 0
		size = 1
		world[y][x] = 'counted land'

		size = size + continent_counter(world, x-1, y-1)
		size = size + continent_counter(world, x , y-1)
		size = size + continent_counter(world, x+1, y-1)

		size = size + continent_counter(world, x-1, y)
		size = size + continent_counter(world, x+1, y)

		size = size + continent_counter(world, x-1, y+1)
		size = size + continent_counter(world, x, y+1)
		size = size + continent_counter(world, x+1, y+1)
		return size

print(continent_counter(world , 5 , 5))


# Homework 4 

for i in range(0, 11):
	for j in range(0, 11):
		print (world[i][j], end = " ")
	print()




