# 1 st Method
n = 1221
n_str = str(n)
left,right = 0,len(n_str)-1
isbool = True
while left < right :
    if n_str[left] != n_str[right] :
        isbool = False
        break
    else:
        left += 1
        right -=1
    isbool = True

print(isbool)
