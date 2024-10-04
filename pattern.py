# Single loop pattern 

def myfun(n):
    for i in range(n):
        print(" "*(n-i) + "* "*i)

myfun(6)