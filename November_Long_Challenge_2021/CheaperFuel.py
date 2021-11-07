def cheapFuel(x, y, a, b, k):
    if x > y and a > b:
        return "DIESEL"
    elif x < y and a < b:
        return "PETROL"
    elif x == y and a == b:
        return "SAME PRICE"
    else:
        for i in range(k):
            x += a
            y += b
        if x < y:
            return "PETROL"
        elif x > y:
            return "DIESEL"
        else:
            return "SAME PRICE"

tc = int(input("test case: "))
for i in range(tc):
    x, y, a, b, k = list(map(int, input("-> ").strip().split()))
    s = cheapFuel(x, y, a, b, k)
    print(s)
