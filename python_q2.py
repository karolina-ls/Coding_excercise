"""Write a function which is passed an integer, n, and returns a list of n lists such that:
f(0) returns []
f(1) returns [[1]]
f(2) returns [[1], [1,2]]
f(3) returns [[1], [1,2], [1,2,3]]
etc."""

def list_generator(n):
    a_list=[]
    list_of_lists=[]
    for i in range(0,n):  
        a_list.append(i+1)
        list_of_lists.append(list(a_list))
    print(f"f({n}) = {list_of_lists}")
list_generator(3)
