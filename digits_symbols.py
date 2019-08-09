# The digits are represented  as symbols.find the difference and sum
n1 = '10'
n2 = '8'

#The ord() function returns the charecter number in symbol table
a = ord(n1)
b  = ord(n2)
#symbols of digits follow one another in the table.therefore,the difference of
#their codes will be the same as the diferrence of digits.

diff = a - b
#if we substract the code of zero from the code of digits,we get the number corresponding
# to the digit charecter.
a = a-ord('0')
b = b-ord('0')
# after that you can sumply find  the sum of the numbers
suma = a + b

print("%s-%s=%d" %(n1,n2,diff))
print("%s+%s=%d" %(n1,n2,suma))
