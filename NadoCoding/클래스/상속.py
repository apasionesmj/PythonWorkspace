# # 일반 유닛
# class Unit:
# 	def __init__(self, name, hp, damage):
# 		self.name = name
# 		self.hp = hp


# # 공격 유닛
# class AttackUnit:
# 	def __init__(self, name, hp, damage):
# 		self.name = name
# 		self.hp = hp
# 		self.damage = damage

# 	def attack(self, location):
# 		print("{0} : {1}방향으로 적군을 공격 합니다.[공격력 {2}]".format(self.name, locatio, self.damage))



# Unit의 멤버변수인 name 과 hp가 AttackUnit에도 있기때문에 상속으로 변경

class Unit:
	def __init__(self, name, hp):
		self.name = name
		self.hp = hp

# class AttackUnit 에서 class AttackUnit(상속받을클래스)으로 변경 후
# Attaqck Unit 내부에 Unit.__init__을 통해 Unit 클래스의 __init__을 가져온다.
# 부모 클래스 Unit, 자식 클래스 AttackUnit
class AttackUnit(Unit):
	def __init__(self, name, hp, damage):
		Unit.__init__(self, name, hp)
		self.damage = damage

	def attack(self, location):
		print("{0} : {1}방향으로 적군을 공격 합니다.[공격력 {2}]".format(self.name, location, self.damage))

	def damaged(self, damage):
		print("{0}이(가) {1} 데미지를 입었습니다.".format(self.name, damage))
		self.hp -= damage
		print("{0}의 현재체력은 {1}입니다.".format(self.name, self.hp))
		if self.hp <= 0:
			print("{0}이 파괴 되었습니다.".format(self.name)) 

firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)