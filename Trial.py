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