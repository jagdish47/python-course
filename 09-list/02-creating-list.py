# Create a list of numbers
numbers = [1,2,3,4,5]
print(numbers)
print(len(numbers))

# Create a list of string
fruits = ["apple","banana","orange","grapes","mango"]

# Mixed datatype
mixing = ["apple", 100, True, 99.99]

# Accessing datt
print(mixing[0])
print(mixing[1])
print(mixing[-1]) #give last value of list
print(mixing[-2]) #give second last value of list


# Update
mixing[1] = "Jagdish"
print(mixing)


# removing/deleting element
del mixing[1]
print(mixing)

mixing.remove(1)
print(mixing)