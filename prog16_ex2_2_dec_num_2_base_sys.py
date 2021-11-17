# Entering a number and converting to an integer
num = int(input())
# Input of the number system
base = int(input("Base (2-9): "))
# Checking the correctness of the number system.
# If the base does not belong to the specified range,
# then the program terminates.
if not(2 <= base <= 9):
 quit()
# Variable for storing a string representation
# of a number in a given number system
newNum = ''
# While the integer is greater than 0,
while num > 0:
 # the remainder from its division into the base is calculated,
 # the rest is converted to the string type and added
 # to the beginning of the string representation of the new number
 newNum = str(num % base) + newNum
 # The decimal number is divided on the basis
 # of the given number system
 num //= base
# Output of the string representation of a number
# in a given number system
print(newNum)
