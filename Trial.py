my_list = ['STRING', 100,23.2]
print(len(my_list))

mylist = ['one', 'two', 'three']
print(mylist[0])
print(my_list[1:])
print(mylist[1:])
another_list = ['four', 'five']
new_list = my_list + another_list
print(new_list)
new_list[0] = 'string'
new_list.append('six')
print(new_list)
new_list.pop()
print(new_list)
print(new_list.pop(0))

num_list = [0, 1, 7, 3, 8, 2, 5, 4, 6, [17,19,18]]
new_list = ['e', 'x', 'w', 'p', 'a', 's', 'n']

new_list.sort()
#num_list.sort()
print(new_list)
print(num_list)
new_list.reverse()
num_list.reverse()
print(num_list)
print(new_list)
print(num_list[-3])

my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict['key1'])
print(my_dict)

fruit_list = {'Apples': '$5.85', 'Banana':'$4.50', 'Mango':'$5.25'}
print(fruit_list['Banana'])

d = {'k1':'first', 'k2':[1,2,3,4,5], 'k3':{'inside_key':100}}
print(d['k3']['inside_key'])
print(d['k2'][3])

m = {'key1':['a','b','c']}
mi_list = m['key1']
print(mi_list)
letter = mi_list[1]
print(letter)
print(letter.upper())

print(m['key1'][2].upper())

p = {'k1':100, 'k2':200}
print(p['k1'])
p['k3'] = 300
print(p)
p['k2'] = 'New Value'
print(p['k2'])
print(p)

print(p.keys())
print(p.values())
print(p.items())

dan = (1,2,3)
bee = [1,2,3]
ife = {'3':23, '2':76, '1':140}
dave = {'31', '30', 'er'}

print(type(dan))
print(type(ife))
print(type(bee))
print(type(dave))

print(dan.count(2))
myset = set()
myset.add(1)
print(myset)
myset.add(2)
myset.add(24)
myset.add('Michael')
print(myset)

mynewlist = [1,1,1,2,2,2,3,3,4,4,4,4,4,5,5,5,5,5]
print(set(mynewlist))

