#===== Write a program that tells you the following :
# - how many hours in a year?
# - how many minutes in a decade?
# - how many seconds old are you?
# - I'm 48618000 seconds old. calculate her age. 
#===== tougher question
# - calculate 
# - how many days does it take for a 32-bit syatem to timeout, if it has a bug with integer overflow?
#   how anout a 64-bit system?

print( 24 * 365 )
print( 60 * 24 * 365 * 10 )
print( 60 * 1 * 60 * 1 * 24 * 365 )
print( 60 * 60 * 24 * 365 * 25 )
#age in years
y = 48618000 / ( 365 * 24 * 60 * 60 )
print( y )


