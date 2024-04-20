

info = {
    "name":"Jagdish Kumawat",
    "age":22,
    "gender":"Male",
    "Contact":"+91-9649294747",
}


print(info['name'])
print(info['age'])
print(info['gender'])
print(info['Contact'])

#using get() method


print(info.get('name'))
print(info.get('age'))
print(info.get('grade')) #if not available -> None 


#Iterating through Keys

for key in info:
    print(f"{key} : {info[key]}")

#Iterating through (key-value pairs)

for key, value in info.items():
    print(f"{key} : {value}")