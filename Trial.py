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

num_list = [0, 1, 7, 3, 8, 2, 5, 4, 6]
new_list = ['e', 'x', 'w', 'p', 'a', 's', 'n']

new_list.sort()
num_list.sort()
new_list.reverse()
print(new_list)
print(num_list)
