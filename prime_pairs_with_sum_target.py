def list_primes(n):
    primes = []
    for i in range(1, n+1):
        if i == 1 or i == 2:
            primes.append(i)
        else:
            for j in range(2, i+1):
                if i % j == 0 and i != j:
                    break
            else:
                primes.append(i)
    return primes

def get_pairs(prime_list, target):
    ans = []
    for i in prime_list:
        for j in prime_list[1:]:
            if target - i == j:
                if sorted([i,j]) in ans:
                    pass
                else:
                    ans.append(sorted([i,j]))
    return ans

n = int(input("Enter a number : "))
print(get_pairs(list_primes(n), n))