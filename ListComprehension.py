Numbers = [3,9,12]

'''Adding Squares of number in Square list
   where num is working as index eg: index:0 == 3 | index:1 == 9..
   And num is adding that item into the list'''

Squares = [num*2 for num in Numbers]

Names = ['David','John','Caroline','Dave','Elanor']

'''Appending names having len greater than five chars and then
   converting into uppercase'''

ShortNames = [name.upper() for name in Names if len(name) >= 5]

print(ShortNames)