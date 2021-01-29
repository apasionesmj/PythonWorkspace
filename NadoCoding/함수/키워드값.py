def profile(name, age, main_lang):
	print(name, age, main_lang)


profile(name = "유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name = "김태호")

#키워드 값을 넣으면 순서가 섞여있어도 초기에 지정한 순서대로 나온다.