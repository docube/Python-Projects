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