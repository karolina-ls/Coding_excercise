""" 
Define a generator which generates the positive integers up to and including a supplied value 
which are divisible by another supplied positive integer and use it to calculate the sum of all 
positive integers less than 102030 which are divisible by 3
"""

def generator(n,m):
    number_list=[]
    """The requirement asks for a generator up to and including a supplied value (=<n), 
    but it's supposed to be used to get number less than (<n). 
    The code returns the number including the limit (so including 102030), 
    but the condition or the argument can be ammended based on the need"""
    for i in range(n+1):
        if i%m==0:
            number_list.append(i)
    result=sum(number_list)
    print(f"The sum of all positive integer up to and including {n} divisible by {m} is: {result}")

generator(102030,3)
