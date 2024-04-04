#Concatenation

str1 = "Hey,"
str2 = "How are you"
greet = str1 + " " + str2
# print(greet)


# String Length -> len("whatever the string it will give you length")
string_len = "Hey how are you"
my_length = len(string_len)
# print(my_length)


#String Indexing and Slicing
text = "Python"
print(text[0]) #first character
print(text[-1]) #last character
print(text[1:4]) #yth -> 4th index won't include

#Formatting string
name="Jagdish"
age=24

formatted_string = f"My Name is {name} and I'm {age} old"
print(formatted_string)

#Escape Character which is new line

escaped_string = "Hey,\n How re you \n are you alright"
print(escaped_string)