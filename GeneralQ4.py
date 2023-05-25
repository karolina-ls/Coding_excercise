"""4. Write a function in a language of your choice which, when passed a decimal digit X, returns the 
value of X+XX+XXX+XXXX. E.g. if the supplied digit is 3 it should return 3702 
(3+33+333+3333)."""

def decDig(x):
    x=str(x)
    strList=[x,x+x,x+x+x,x+x+x+x] 
    intList=[]
    for y in strList:
        y=int(y)
        intList.append(y)
    print(f"({intList[0]} + {intList[1]} + {intList[2]} + {intList[3]}) = {sum(intList)}")       
decDig(3)