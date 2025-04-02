a = 35
b = 7
c = 2

# if a <= b and b <= c: # same as below 
if a <= b <= c:
    print(a, b, c)
elif a <= c <= b:
    print(a, c, b)
elif b <= a <= c:
    print(b, a, c)
elif b <= c <=a:
    print(b, c, a)
elif c <= a <= b:
    print(c, a, b)
else: # only version with c <= b <= a remains
    print(c, b, a)