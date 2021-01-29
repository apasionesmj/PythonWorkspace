# print("python", "java" , sep=",", end="?") #sep=seperate ""안에 들어간 문자열로 구분 #end 앞에 문장의 끝부분을 ""안에 들어간 문자열을 쓰고 뒤에 문장을 이어서 한문장으로 출력
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout) #표준 출력
# print("Python", "Java", file=sys.stderr) #표준 에러

#시험 성정
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items():
# 	#print(subject, score)
# 	print(subject.ljust(8), str(score).rjust(4), sep=":") #과목명은 과목명을 포함한 8칸을 확보하고 왼쪽정렬, 점수는 점수를 포함한 4칸을 확보하고 오른쪽정렬


# 은행 대기순번표
# 001, 002, 003, ....
# for num in range(1,21):
# 	print("대기번호 : " +str(num).zfill(3)) #3개의 공간을 확보하고 나머지 빈공간은 0으로 채운다

# 표준입력
answer = input("아무 값이나 입력하세요 : ") #input을 통해서 값을 받으면 항상 문자열로 받아진다.
print(type(answer))
print("입력하신값은" +answer+"입니다.")
