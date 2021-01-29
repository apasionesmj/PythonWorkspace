# 쓰기 "w" write
# score_file = open("score.txt", "w", encoding="utf8")
# print("수학:0", file=score_file)
# print("영어:50", file=score_file)
# score_file.close()


# 이어서 쓰기 "a" append
# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# print("영어:50", file=score_file)
# print("과학:50", file=score_file)
# score_file.close()


# 읽어 오기 "r" read
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()


# 한줄한줄 처리
# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline()) # 줄별로 일기, 한줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline(), end="") # 줄바꿈이 필요 없을때
# print(score_file.readline())
# score_file.close()


# 몇줄인지 모를때 처리, line 읽기를 while 지속하다가 line이 더이상 없다면 break 후 출력
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
# 	line = score_file.readline()
# 	if not line:
# 		break
# 	print(line, end="")
# score_file.close()


# 리스트에 넣어서 처리
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
	 print(line, end="")
score_file.close()