import random
n = 200
flag_num = random.randint(0, n)
print(flag_num)
def get_flag_num(your_num):
    if your_num > flag_num:
        return -1
    elif your_num < flag_num:
        return 1
    else:
        return 0
        
        
def enter_number(entered_num):
    start, end = 0, entered_num 
    while start <= end:
        avg = (start + end) // 2
        if get_flag_num(avg) == 0:
            return avg
        elif get_flag_num(avg) == 1:
            start = avg + 1
        elif get_flag_num(avg) == -1:
            start -= 1
            
    return get_flag_num(entered_num)
    
ans = enter_number(n)
print(ans)