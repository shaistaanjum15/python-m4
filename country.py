country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977'}
 
# search dictionary for country code of India
print("Country code for India -")
print(country_code.get('India', 'Not Found'))
 
# search dictionary for country code of Japan
print("Country code for Japan -")
print(country_code.get('Japan', 'Not Found'))


my_set = {1, 2, 3, 3, 4, 5, 5, 5}
print(my_set)

my_set = {1, 2, 3}
my_set.add(7)
print(my_set)

#intersection blue is common in both 
setx = {"green", "blue"}
sety = {"blue", "yellow"}
setz = setx.intersection(sety)
print(setz)

import array as arr
a = arr.array('i', [1, 2, 3])
print(a)