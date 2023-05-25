"""2. Write a function in a language of your choice which, when passed two sorted arrays of integers
returns an array of any numbers which appear in both. No value should appear in the returned
array more than once."""

def commonArray(a,b): 
    a.sort()
    b.sort() 
    newarray = []
    for x in array1:
        for y in array2:
            if x == y and y not in newarray:
                newarray.append(x)
    print(f"Common integers in array: {array1} and {array2} are: {newarray}")
array1  =[11, 2, 33, 3, 5, 8]
array2 = [1, 3, 8, 10]
commonArray(array1, array2)


