# 모듈 -- 필요한 것들끼리 부품처럼 잘 만들어진 파일, 유지보수를 쉽게하고 코드의 재사용을 가능케하는.
# ex) 자동차의 타이어, 범퍼 등 교체가 가능한 것들
# 함수 정의나 클래스 등의 파이썬 문장을 담고 있는 파일들.

# import theater_module
# theater_module.price(3) #3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) #4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5) #5명이서 군인 할인 영화 보러 갔을 때


# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5) 

# from theater_module import price, price_morning
# price(5)
# price_morning(6)

from theater_module import price_soldier as ps
ps(5)