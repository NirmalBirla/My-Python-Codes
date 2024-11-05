# Single loop pattern 

def myfun(n):
    for i in range(1, n+1):
        print(" "*(n-i) + "* "*i)

num = int(input("Enter a number  : "))
myfun(num)