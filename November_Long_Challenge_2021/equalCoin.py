tc = int(input())
for i in range(tc):
    x, y = list(map(int, input().strip().split()))
    if x % 2 == 0:
        if x == 0 and y % 2 != 0:
            print("NO")
        else:
            print("YES")
    else:
        print("NO")