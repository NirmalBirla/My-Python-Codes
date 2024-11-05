stones = [3,1,100]
while len(stones)>1:
    stones.sort()
    x = stones[-2]
    y = stones[-1]
    
    stones.remove(x)
    stones.remove(y)
    
    if x == y:
        pass
    else:
        stones.append(y-x)
    
if len(stones) == 0:
    stones.append(0)
else:
    print(stones[0])