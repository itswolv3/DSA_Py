# o(n)
def print_items(n):
    for i in range(n):
        print(i)

# This runs o(2n), we can drop the constant and say o(n)
def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)


# o(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

# It doesn't matter how many nested loops we run this
# through it will still be o(^2)

# Drop non-dominants
# If we look at the code below, we can see it runs o(n^2)
# for a one section and o(n) for the other. We could say
# this runs o(n^2 + n) but we simplify by just saying o(n^2)
# and drop the n as it is not the dominant time factor n^2 is.
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
   
    for k in range(n):
        print(k)


# o(1) or contant time
def add_items(n):
    return n + n
# we only perform one operation, this is the most optimal

# o(log n)
def find_x(arr, x):
    res = arr
    while len(res) != 1:
        split = len(res) // 2
        
        if x in res[:split]:
            res = res[:split]
        else:
            res = res[split:]

    print(res)

# Different terms for inputs
# If we look at the code below we can see 2 arguments
# passed into the code, we might think it would be o(2n) which
# becomes o(2), but as the the arguments could be different numbers
# the most simplistic way to simplify this down is o(a + b)
# o(a + b)
def print_items(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

# o(a * b)
def print_items(a, b):
    for i in range(a):
        for j in range(a):
            print(i, j)


# Lists
my_list = [11, 3, 23, 7]

# o(1) operations on a list
my_list.pop()
my_list.append(7)

# o(n) operations
my_list.pop(0)
my_list.insert(0, 11)
# Both the methods above perform a single operation to add or remove the item
# and then have to perform operations to re-index the list afterwards
