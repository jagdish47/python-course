my_list = [1,2,3,4,5]

my_list.append(10) #adding at last
print(my_list)

my_list.extend([100,200,300]) #adding multiple values at last
print(my_list)


my_list.insert(1, 99) #index 1 add 99
print(my_list)

my_list.remove(1)
print(my_list)


my_list.pop()
print(my_list)


my_list.sort()
print(my_list)


copy_list = my_list.copy()
print(copy_list)

