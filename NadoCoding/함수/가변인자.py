#일반적인 방법
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
# 	print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ") #end=" "   문장이 끝나고 난후 줄바꿈 없이 "" 안에 내용 출력후 다음문자 바로 이어서 나오기
# 	print(lang1, lang2, lang3, lang4, lang5)
	

#가변인자 사용시
def profile(name, age, *language):
	print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ") #end=" "   문장이 끝나고 난후 줄바꿈 없이 "" 안에 내용 출력후 다음문자 바로 이어서 나오기
	for lang in language:
		print(lang, end=" ")
	print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Kotlin")
profile("김태호", 25, "Script", "Ruby", "", "", "")
