# 일반 구구단
for x in range(2,10):
    print(f"===={x}단====")
    for y in range(1,10):
        print(x, "*", y , "=", x*y)


# 3중 반복 구구단
z = input()
v = 2
while (9 >= v):
    print()
    for x in range(1,10):
        for y in range(int(z)):
            if(y+v < 10) :
                print(y+v, "*", x, "=", (y+v)*x, end="\t")
        print()
    v += int(z)
