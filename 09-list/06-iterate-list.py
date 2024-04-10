my_list = [3,5,10,3,55,4,2]

#using for in loop
for element in my_list:
    print(element)

#using for loop
for i in range(0, len(my_list)):
    print("index : ",i ," : ",my_list[i])

#using while loop
i = 0
while(i < len(my_list)):
    print(my_list[i])
    i+=1