#tuple - 리스트와 비슷하지만 변경 불가. but, 속도가 훨씬 빠름
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") -> 실행 안됨. 값을 추가하는 것은 불가능.
# name = "김종국"
# age = "20"
# hobby = "코딩"
# print(name, age, hobby)

#tuple은 한번에 선언이 가능함.
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)


