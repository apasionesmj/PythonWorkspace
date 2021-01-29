# def profile(name, age, main_lang):
# 	print("이름 : {0} \t나이 : {1} \t 주사용언어 : {2}"\
# 		.format(name,age,main_lang)) #역슬러쉬(\)는 줄바꿈할때 사용가능

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")



#같은 학교 같은학년 같은반 같은수업이라면 기본값 사용
def profile(name, age=17, main_lang="파이썬"):
	print("이름 : {0} \t나이 : {1} \t 주사용언어 : {2}"\
		.format(name,age,main_lang))

profile("유재석")
profile("김태호")