# write a recursive function to calculate sum of n  natural odd number
def sum_odd(n):
    if n == 0:
        return 0
    s = 2*n-1 + sum_odd(n-1)
    return s

print(sum_odd(5))

# write a recursive function to calculate sum of n even number
def sum_even(n):
    if n == 0:
        return 0
    s = 2*n + sum_even(n-1)
    return s

print(sum_even(5))

#write recursive function to caluculate sum of n natural number
def sum_n(n):
    if n == 0:
        return 1
    s = n + sum_n(n-1)
    return s

print(sum_n(10))

# Write a function to calculate factorial of a number
def fact_n(n):
    if n == 0:
        return 1
    fact = n*fact_n(n-1)
    return fact

print(fact_n(5))

# Write a function to calculate the sum of square of n natural number 
def square_n(n):
    if n == 1:
        return 1
    s = n**2 + square_n(n-1)
    return s

print(square_n(5)) 

