def butterfly_pattern(n):
    for i in range(1, n+1):
        print("* "*i + "  "*((n-i)*2) + "* "*i)
    
    for j in range(1, n):
        print("* "*(n-j) + "  "*(j*2) + "* "*(n-j))


n = int(input("Enter a number : "))
butterfly_pattern(n)