"""3. Write a function in a language of your choice which, when passed a positive integer returns 
true if the decimal representation of that integer contains no odd digits and otherwise returns 
false."""

def oddEven(x):
    digList = [int(x) for x in str(x)]
    for y in digList:
        if y%2!=0:
            check = False
            break
        else:
             check = True
    print(f"Positive integer {x} contains no odd digits: {check}")          
oddEven(822348)