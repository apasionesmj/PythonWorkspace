
# for i in range(5):          # 5번 반복. 바깥쪽 루프는 세로 방향
#     for j in range(5):      # 5번 반복. 안쪽 루프는 가로 방향
#         print('j:', j, sep='', end=' ')    # j값 출력. end에 ' '를 지정하여 줄바꿈 대신 한 칸 띄움
#     print('i:', i, '\\n', sep='')    # i값 출력, 개행 문자 모양도 출력
#                                      # 가로 방향으로 숫자를 모두 출력한 뒤 다음 줄로 넘어감
#                                      # (print는 기본적으로 출력 후 다음 줄로 넘어감)

# for x in range(1, 10):
#     for z in range(1, 3):
#         for y in range(1, 4):
#             print(y, " * ", x, " = ", y * x, end="\t")
#         print()
        



# z = input()

# for i in range(2,10):
#     for j in range(1,2):
#         for z in range(int(z)):
#             print(z, "*", i, "=", z*i , end="\t")
#         print()

# z = input()

# for x in range(1,10):
#     for y in range(int(z)):
#         print(y+2, "*", x, "=", (y+2)*x, end="\t")
#     print()


# z = input()
# v = 1
# for a in range(9):
#     for x in range(2,10):
#         for y in range(int(z)):
#             print(y+1, "*", x, "=", (y+1)*x, end="\t")
#         print()
#     v += int(z)

z = input()
v = 1
while (9 >= v):
    for x in range(2,10):
        for y in range(int(z)):
            print(y+v, "*", x, "=", (y+v)*x, end="\t")
        print()
    v += int(z)
