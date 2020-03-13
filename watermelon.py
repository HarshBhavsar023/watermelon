w = int(input())
if w>=1 and w<=100:
    a = w%2
    b = a%2
    if w==2:
        print("NO")
    elif b%2==0:
        print("YES")
    else:
        print("NO")
else:
    print("NO"
