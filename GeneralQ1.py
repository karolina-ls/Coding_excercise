"""1.The Fibonacci sequence is defined as a sequence of integers starting with
1 and 1, where each
subsequent value is the sum of the preceding two. I.e.
f(0) = 1
f(1) = 1
f(n) = f(n-1) + f(n-2) where n >= 2
Write a program in a language of your choice to calculate the sum of the first
100 even-valued
Fibonacci numbers."""

n0, n1 = 1, 1
nth = 0
sum1 = 0
count = 0
limit: int = 100
while count < limit:
    nth = n0 + n1
    if nth %2 == 0:
        count += 1
        sum1 = sum1 +nth
    n0 = n1
    n1 =nth
print(f"The sum of the first {limit} even-valued Fibonacci numbers is: {sum1}")