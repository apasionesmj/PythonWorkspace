# # 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린"
# hp = 40
# damage = 5

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1} 입니다.\n".format(hp, damage))


# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
 
# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1} 입니다.\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35
 
# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1} 입니다.\n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
# 	print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

#일반유닛
class Unit:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage
		print("{0} 유닛이 생성 되었습니다.".format(self.name))
		print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))


# # 객체 : class를 통해 만들어지는 marine1, marine2, marine3, tank 같은 것들
# # marine1,2,3,tank는 unit 클래스의 인스턴스 
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# marine3 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 5)

# # __init__ 생성자
# # 객체가 만들어질때 자동으로 호출되는 부분
# # 객체를 생성될때 기본적으로 init함수에 정의된 파라미터 갯수와 동일하게 적용해야한다.

# # 멤버변수
# # 클래스 내에서 정의된 변수(class Unit에서 name, hp, damage)
# # 멤버변수를 외부에서도 사용가능 ex. wraith.name 
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# wraith2 = Unit("레이스2", 80, 5)
# wraith2.clocking = True #외부에서 추가로 변수를 할당 wraith2에는 있지만 wraith1에는 없음.

# if wraith2.clocking == True:
# 	print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))


# 공격유닛
class attackUnit :
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage
	
	#self는 자기자신을 나타냄. class내에서 메소드(첫번째)는 반드시 self로 한다.
	def attack(self, location):
		print("{0}이(가) {1} 방향으로 적군을 공격 합니다.[공격력은 {2} 입니다.]".format(self.name, location, self.damage))

	def damaged(self, damage):
		print("{0}이(가) {1} 데미지를 입었습니다.".format(self.name, damage))
		self.hp -= damage
		print("{0}의 현재체력은 {1}입니다.".format(self.name, self.hp))
		if self.hp <= 0:
			print("{0}이 파괴 되었습니다.".format(self.name)) 

firebat1 = attackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)


