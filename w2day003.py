# Week 2 day 3
#  Dictionaties - notation {} , constructor 

# constructor 
dictionaryConstructor = dict(name = "Pubz", discordId = "xxxxx", favFood = "Ice Cream")
print(dictionaryConstructor)
# notation
myDict = {
	"a" : 3500,
	"b" : 1500,
	"c" : 400
}

print(myDict)

# access

print(myDict["a"])

# add
myDict["p"] = 500
print(myDict["p"])
# modify

myDict["a"] = 4000

# delete item
del(myDict["p"])

# delete dictionary

# del(myDict)
print(myDict)




# homework 01 

# Modify 'a' for another value name in mydict.
myDict["new"] = myDict.get("a")
del(myDict["a"])
# myDict.pop("a") << this also works
print(myDict)

# redo the frequency distribution of alice_in_wonderland.txt and save your results in a dictionary.

alice = {}

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

with open("alice_in_wonderland.txt") as f:
    contents = f.read().lower()
for i in range(len(alphabet)):
	alice[alphabet[i]] = str(contents.count(alphabet[i]))

print(alice)
#  create a dictionary with your own personal details , fell free to be creative and funny. Practice adding , modifying accesing

hereIam = dict(name = "Pubz", age = "xoxo", hometown = "Matara, Sri Lanka", favFood = "Pasta", favDrink = "Faluda", favThing = "Break the codes")

#  [Optional/Advanced] Write a test to check the outcome of the alice_in_wonderfland task: one test for list of lists, and one test for dictionary output


# #### Classes
class Student():
	def __init__(self, stuID, favFood):
		self.studentID = stuID
		self.favouriteFood = favFood
	def print(self):
		print(self.studentID +" "+ self.favouriteFood)

s1 = Student("0001", "Ice Crem")
s2 = Student("0002", "Pasta")
print(s1.studentID, s1.favouriteFood)
s2.print()

# del s1.favouriteFood   
# del s1


# home work 2

class Student1MWTT():
	def __init__(self, firstName, lastName, email, countryCode, phoneNumber, gitHub, country, purpose, codingLevel, joiningGroup, studentType):
		self.firstName = firstName
		self.lastName = lastName
		self.email = email
		self.countryCode = countryCode
		self.phoneNumber = phoneNumber
		self.gitHub = gitHub
		self.country = country
		self. purpose = purpose
		self.codingLevel = codingLevel
		self.joiningGroup = joiningGroup
		self.studentType = studentType

member1 = Student1MWTT("Mikky", "Mouse", "mikkymouse@email.com", "01", "0123564789", "/github.com/mikky", "America", "1", "2", "1,2,3,10", "1,2")

print(member1.firstName)