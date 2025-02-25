def gibonacci(n, x, y):
    ans = [x,y]
    a, b = x, y
    for _ in range(2, n):
        a, b = b, a - b
        ans.append(b)
    return ans

def fibonacci(n, x, y):
    ans = [x,y]
    a, b = x, y
    for _ in range(2, n):
        a, b = b, a + b
        ans.append(b)
    return ans

n = int(input("Enter number of terms you want to print : "))
a = int(input("Enter first term : "))
b = int(input("Enter second term : "))

print("Gibonacci ", gibonacci(n,a,b))
print("Fibonacci ", fibonacci(n,a,b))