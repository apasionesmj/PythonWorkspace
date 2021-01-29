# 다중 상속이란 부모클래스가 여러개인 것
# ex) 공중 유닛은 일반 유닛에 공격이 가능하고, 드랍쉽의 경우 일반 유닛에 공격이 불가능.

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))


# 공격 유닛
class AttackUnit(Unit):    # Unit이 부모클래스 AttackUnit이 자식클래스 
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} :  현재체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴 되었습니다.".format(self.name)) 

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed   #멤버변수 초기화

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도는 {2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):   # 다중 상속은 , 로 구분하면 된다.
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed = 0
        Flyable.__init__(self, flying_speed)
    #move라는 함수를 새롭게 정의(오버로딩)
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit("별쳐", 80, 10, 20)

# 배틀크루저 : 공중유닛, 체력도 높고, 공격력도 높음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
battlecruiser.move("9시")