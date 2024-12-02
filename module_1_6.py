my_dict = {"Nur": 1998}
print(my_dict)
print(my_dict.get("Nur"))
print(my_dict.get("Alex"))
my_dict.update({"Anton": 1995,"Sergey": 2000})
print(my_dict)
a = my_dict.pop("Nur")
print(a)
print(my_dict)
my_set = {1,1,1,1,2,3,2,2,3,3,5,}
print(my_set)
my_set.update({6,8})
my_set.remove(1)
print(my_set)