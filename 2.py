USD_to_GBP = 0.66    # today's exchange rate
GBP_sign = '\u00A3'  # Unicode value for pound
dollars = 1000        # Number dollars to convert

#USD_to_GBP = 'abc'
# Conversion calculations
pounds = dollars * USD_to_GBP
print(pounds)
# Printing the results
print('Today, $' + str(dollars))
print('converts to ' + GBP_sign + str(pounds))


