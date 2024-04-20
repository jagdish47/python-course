info = {
    "name":"Jagdish Kumawat",
    "age":22,
    "gender":"Male",
    "Contact":"+91-9649294747",
}

#deleteing name
del info['name']
print(info)

#delete using pop
info.pop("age") #atlest one argument require
print(info)

#deleting last item
info.popitem()
print(info)


#deleting complete dictionary
info.clear()
print(info)