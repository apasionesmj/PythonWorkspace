#당첨자 뽑기 이벤트
#1명은 치킨, 3명은 커피,
#조건 1 : 댓글은 20명이 작성하였고 아이디는 1~20
#조건 2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
#조건 3 : random모듈의 shuffle과 sample 을 활용

#출력 예제
# ---당첨자 발표 ---
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# ---축하합니다. ---

#활용 예제
from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,1))

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# lst = range(1,21) 1부터 20까지 숫자를 생성.
print(lst)
shuffle(lst)
print(lst)

winners = sample(lst, 4) #4명중에서 1명은 치킨 3명은 커피
print("---당첨자 발표 ---")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--- 축하 합니다. ---")
