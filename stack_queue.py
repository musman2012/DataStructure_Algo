## Stack and Queue are popular data structures which can be implemented using Lists in Python
## After appending the items in list, if we keep doing pop() last element in the list will be removed --> LIFO --> Stack
## To make a list work like a Queue, we call pop() with 0 as argument. list.pop(0) will remove the first index --> FIFO --> Queue

test_arr = ['1','2','3','4','5','11','12','13','14','15']

for i in range(0,5):
    print(test_arr.pop(), " ----- ", test_arr.pop(0))
    
'''
Output:
15  -----  1
14  -----  2
13  -----  3
12  -----  4
11  -----  5

'''
