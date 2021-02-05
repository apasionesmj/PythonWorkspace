# 백준 별찍기 -1(2438번) n째줄에는 n개의 별이
# num = int(input())
# for i in range(1,(num+1)):
#     print("*"*i)

# 백준 별찍기 -2(2439번) n째줄에는 n개의 별이 오른쪽 정렬
# num = int(input())
# for i in range(1,num+1):
#     print(("*"*i).rjust(num))

# 백준 별찍기 -3(2440번) 1번째 줄 n개, 2번째줄 n-1개, 3번째줄 n-2개
# num = int(input())
# for i in reversed(range(1, num+1)):
#     print("*"*i)

# 백준 별찍기 -4(2441번) 1번째 줄 n개, 2번째줄 n-1개, 3번째줄 n-2개 오른쪽 정렬
# num = int(input())
# for i in reversed(range(1,num+1)):
#     print(("*"*i).rjust(num))

# 백준 별찍기 -5(2442번) n번째 줄에 별 2xn개-1개 찍기 가운데 정렬 사용
# num = int(input())
# for i in range(1, num+1):
#     print(("*"*(i*2-1)).center(num*2-1))

# 백준 별찍기 -6(2443번) 2442번 리버스
# num = int(input())
# for i in reversed(range(1,num+1)):
#     print(("*"*(i*2-1)).center(num*2-1))

# 백준 별찍기 -7(2444번) 다이아몬드 찍기
# num = int(input())
# for i in range(1,num+1):
#     print(("*"*(i*2-1)).center(num*2-1))
# for i in reversed(range(1,num)):
#     print(("*"*(i*2-1)).center(num*2-1))

# 백준 별찍기 -8(2445번) 리본 찍기
# num = int(input())
# for i in range(1,num+1):
#     print("*"*i+" "*(num-i)+("*"*i).rjust(num))
# for i in reversed(range(1,num)):
#     print("*"*i+" "*(num-i)+("*"*i).rjust(num))

# 백준 별찍기 -9(2446번) 모레시계 찍기
# num = int(input())
# for i in reversed(range(1, num+1)):
#     print(("*"*(i*2-1)).center(num*2-1))
# for i in range(1, num):
#     print(("*"*(i*2+1)).center(num*2-1))

# 백준 별찍기 -10(2447번)====================================실패
# num = int(input())
# for i in range(1,num+1):
#     print("*"*num)

# 백준 별찍기 -11(2448번)====================================실패

# 백준 별찍기 -12(2522번) 리본 오른쪽 반만
# num = int(input())
# for i in range(1,num+1):
#     print(("*"*i).rjust(num))
# for i in reversed(range(1,num)):
#     print(("*"*(i)).rjust(num))

# 백준 별찍기 -13(2523번) 리본 왼쪽 반만
# num = int(input())
# for i in range(1, num+1):
#     print(("*"*i).ljust(num))
# for i in reversed(range(1, num)):
#     print(("*"*i).ljust(num))

# 백준 별찍기 -14(2556번)====================================실패

# 백준 별찍기 -15(10990번) 1번째 줄에 별 1개, 2번째 줄에 별 2개
# num = int(input())

# for i in range(1,num+1):
#     if i < 2:
#         print(("*"*i).center((num)*2-1))
#     else:
#         print(("*" + " "*((i-1)*2-1) + "*").center((num)*2-1))

# 백준 별찍기 -16(10991번) 10990번 업그레이드
# num = int(input())

# for i in range(1, num+1):
#     if i < 2:
#         print(("*"*i).center(num*2-1))
#     else:
#         print(("*" + (" *")*(i-1)).center(num*2-1))

# 백준 별찍기 -17(10992번) 10991번 업그레이드
# num = int(input())

# for i in range(1, num+1):
#     if i < 2:
#         print(("*"*i).center(num*2-1))
#     elif i is not num:
#         print(("*"+" "*((i-1)*2-1)+"*").center(num*2-1))
#     else:
#         print("*"*(num*2-1))

# 백준 별찍기 -18(10993번)====================================실패

# 백준 별찍기 -19(10994번)====================================실패

# 백준 별찍기 -20(10995번)
# num = int(input())

# for i in range(1, num+1):
#     if i%2 == 0:
#         print(" *"*num)
#     else:
#         print("* "*num)

# 백준 별찍기 -21(10996번)
num = int(input())
