#empty dictionary

empty_dict = {}
print(type(empty_dict))


#key-value pair

information = {
    "name":"Jagdish Kumawat",
    "age":20,
    "grade":"A"
}

print(information)


#using the dict() Constructor

person = dict(name="anshu",age=2, city="vada")
print(person)


#Nested Dictionary

nested_dict = {
    "person":{
        "name":"Rahul Kumawat",
        "age":22,
        "gender":"male",
        "location":{
            "country":"India",
            "state":"Rajasthan",
            "city":"Rajsamand",
            "pin":313330,
        }

    }
}

print(nested_dict)