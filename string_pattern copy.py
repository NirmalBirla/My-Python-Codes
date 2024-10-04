s = 'a2b3nirmal5$%2'
ans = ""
c = ""
for i in s:
    try:
        a = int(i)
    except ValueError:
        c = c + i
    else:
        ans += c * a
        c = ""
print(ans)