# Recursive function to write first n natural number
def print_n(n):
    if n <= 0:
        return 
    print_n(n-1)
    print(n)

print_n(10)

# Recursive functon to write first n natural numbers in reverse oder
def print_rn(n):
    if n <= 0:
        return
    print(n)
    print_rn(n-1)

print_rn(10)

# Recursive function to print first n odd number
def odd_n(n):
    if n <= 0:
        return
    odd_n(n-1)
    print(2*n-1)

odd_n(5)

#Recursive Function to print first n even number
def even_n(n):
    if n <= 0:
        return 
    even_n(n-1)
    print(n*2)

even_n(5)

# Recursive function to print first n odd number in reverse order
def odd_rn(n):
    if n <= 0:
        return 
    print(2*n-1)
    odd_rn(n-1)

odd_rn(5)
    
# Recursive function to print first n even nunber in reverse order
def even_rn(n):
    if n == 0:
        return 
    print(n*2)
    even_rn(n-1)

even_rn(5)