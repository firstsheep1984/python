s = 'Hello World!'
print(s)
##################################################################
my_integer = 5
my_flaotaing_point = 26.2
my_Boolean = True
my_string = 'characters'
my_integer = 0xFF

print(0xFF)    # Prints  255
##################################################################
print(3 + 4)   # Prints  7
print (5 - 6)  # Prints -1
print(7 * 8)   # Prints 56
print(45 / 4)  # Prints 11.25
print(2 ** 10) # Prints 1024
##################################################################
s = 'hello' + 'world'
print(s)       # Prints helloworld
s = s * 4
print(s)       # Prints helloworldhelloworldhelloworldhelloworld
##################################################################
# A converter for currency exchange:
USD_to_GBP = 0.66   # Today's exchange rate
GBP_sign = '\u00A3' # Unicode value for £
dollars = 1000      # Number dollars to convert

# Conversion calculations:
pounds = dollars * USD_to_GBP

# Printing the results:
print('Today, $' + str(dollars))               # Today, $1000
print('converts to ' + GBP_sign + str(pounds)) # converts to £660.0
##################################################################

##################################################################