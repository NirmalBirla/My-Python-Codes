stones = [7,4,8,3,1]
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
    
print(stones[0])
