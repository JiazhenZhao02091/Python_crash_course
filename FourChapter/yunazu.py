dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)
age = 10
if age > 10:
    print("age > 10")
elif age == 10:
    print("age == 10")
else:
    print("age < 10")


alien_0 = {'color' : 'green', 'name' : 'Steve', 'points' : 10}
print(alien_0)
print(type(alien_0))

person = {
    "name": "person",
    "age": 18,
    "tel": 123456789
}
print(person)
for key, value in person.items():
    print(key)
    print(value)

for index in person:
    print(index)


number = {
    1: '1',
    2: '2',
    3: '3',
    4: '4'
}
print(number)
num = number.keys()
if 1 in num:
    print("Hava 1 ")
else:
    print("Don't have 1")

list = [1,2,3,4,5,1]
print(list)
set_list = set(list)
print(set_list)
print(type(set_list))