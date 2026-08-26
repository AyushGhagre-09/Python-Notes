info={
    "name":"Ayush",
    "age":25,
    "course":"Python"
}


# it will give error if key not found
print(info["name"])
# it will not give error if key not found
print(info.get("name"))
# modify
info["name"]="Piyush"
# add
info["city"]="Pune"
print(info)

# del info["course"]
# info.pop("course")
# info.popitem()
# info.clear()
print(info)


if "name" in info:
    print("name is present")

# default will be keys
for key in info:
    print(key)


for value in info.values():
    print(value)

print(info.items())
for key,value in info.items():
    print(key,"-",value)

print(len(info))

squared_num={x:x**2 for x in range(1,6)}
print(squared_num)


keys= ["Masala", "Ginger", "Lemon"]

default_value="Delicious"
new_dict=dict.fromkeys(keys,default_value)
print(new_dict)

# keys(), values(), items(), 
# get(),
#  update()
# info.update({
#     "name":"Piyush",
#     "city":"pune"
# })
# , pop(), 
# popitem(), clear(), copy()


# get will not give error if key  is not present