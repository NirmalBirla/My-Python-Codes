x = [i for i in range(1,101)]
def func(x):
    l = x.pop(0)
    x.append(l)
    x.pop(0)
    if len(x)>1:
        func(x)
    return x[0]
print(func(x))