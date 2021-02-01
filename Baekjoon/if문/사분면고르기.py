# 좌표가 (12,5)인 
# 점 A는 x좌표와 y좌표가 모두 양수이므로 제 1사분면에 속한다.
# 점 B는 x좌표가 음수이고 y좌표가 양수이므로 제 2사분면에 속한다.
# 점 C는 x좌표가 음수이고 y좌표가 음수이므로 제 3사분며에 속한다.
# 점 D는 x좌표가 양수이고 y좌표가 음수이므로 제 4사분면에 속한다.

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1사분면")
elif x < 0 and y > 0:
    print("2사분면")
elif x < 0 and y < 0:
    print("3사분면")
else:
    print("4사분면")
