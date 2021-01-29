# 패키지 -- 모듈들을 모아놓은 집합
# import travel.thailand # import를 쓸때는 맨뒤 부분은 모듈이나 패키지만 가능함, 클래스나 함수는 import를 직접할 수 없음. ex) import travel.thailand.TailandPackage   는 불가
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()


# from travel.thailand import ThailandPackage # from import 구문에서는 클래스나 함수를 직접 import할 수 있음.
# trip_to = ThailandPackage()
# trip_to.detail()

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()