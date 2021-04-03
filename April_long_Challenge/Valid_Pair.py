s = list(map(int, input().split(" ")))
s_set = set(s)
if len(s) > len(s_set):
    print("YES")
else:
    print("NO")
