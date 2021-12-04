# This is not m

manuscript = '100 000 000 000 000 000 079'
number_of_zeros = manuscript.count('0')

x = '6' * (number_of_zeros-1) + '716'
y = '3' * number_of_zeros + '63'

print(f'{x}, {y}')
