numbers = [1,2,3,4,5,6,7,8,9,10]

subset = numbers[2:6] #start 2 and 6(not included)
print(subset)

subset = numbers[2:] #start 2 till last
print(subset)


subset = numbers[:5] #start to 5th(not included)
print(subset)

subset = numbers[-4:] #give last 4 elementd
print(subset)


subset = numbers[:-2] #from start to till last 2
print(subset)

subset = numbers[1:-1:3] #from 1 to last and 3 means skip 2 element if there is 2 means skip one element
print(subset)