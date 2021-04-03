import math

test_case = int(input("-> "))
ip_list = list()
for i in range(test_case):
    ip_list.append(list(map(float, input("-> ").split(" "))))

for i in ip_list:
    sp = round((100 / math.prod(i)), 2)
    if sp < 9.58:
        print("YES")
    else:
        print("NO")
