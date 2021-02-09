# Numpy
# 다차원의 배열을 효과적으로 처리할 수 있게 해주는 라이브러리.
# List에 비해 빠르고 강력한 기능을 제공.
# 1차원의 데이터 = Vector, 2차원의 데이터 = Matrix(행렬), 3차원 이상의 데이터 = Tensor
# 1차원의 축(행) axis 0, 2차원의 축(열) axis 1, 3차원의 축(채널) axis 2

# List를 Numpy로 바꿔보기
import numpy as np

# list_date = [1,2,3]
# numpy_array = np.array(list_date)
# print(numpy_array.size)     #데이터의 갯수
# print(numpy_array.dtype)    #자료형
# print(numpy_array[2])       #인덱스로 접근가능

# # Numpy 배열 초기화
# # 0부터 3까지의 배열 만들기
# array1 = np.arange(4)
# print(array1)

# # 모든값이 0으로 초기화된 4*4 크기의 실수형 2차원 배열을 만든다.
# array2 = np.zeros((4, 4),dtype=float)
# print(array2)

# # 모든값이 1로 초기화된 3*3 크기의 문자형 2차원 배열을 만든다.
# array3 = np.ones((3, 3),dtype=str)
# print(array3)

# # 0부터 9까지의 수로 랜덤하게 초기화 된 3*3 크기의 배열 만든다.
# array4 = np.random.randint(0, 10, (3,3))
# print(array4)

# # 평균이 0이고, 표준편차가 1인 표준 정규를 띄는 3*3크기의 배열을 만든다.
# array5 = np.random.normal(0, 1, (3,3))
# print(array5)

# # 배열 합치기(가로축으로 합치기)
# array1 = np.array([1,2,3])
# array2 = np.array([4,5,6])
# array3 = np.concatenate([array1, array2])
# print(array3.shape) # 크기
# print(array3)

# # 배열 형태 바꾸기
# array1 = np.array([1,2,3,4])    # 1차원 배열에서
# array2 = array1.reshape((2,2))  # 2차원 배열로
# print(array2)


# # 세로축으로 합치기
# # np.arage(n) 0부터 n-1까지의 숫자 배열을 1*4 1차원 배열로
# array1 = np.arange(4).reshape(1,4)
# # np.arage(n) 0부터 n-1까지의 숫자 배열을 2*4 2차원 배열로
# array2 = np.arange(8).reshape(2,4)
# print(array1)
# print(array2)
# # 1*4 배열과 2*4 배열이 합쳐져서 3*4배열로
# array3 = np.concatenate([array1,array2], axis=0)
# print(array3)

# # 배열 나누기
# array = np.arange(8).reshape(2,4)
# # 배열을 인덱스[2]를 기준으로 나누고 인덱스[2]는 열(axis=1)을 의미한다.
# left, right = np.split(array, [2], axis=1)
# print(left)
# print(left.shape)
# print(right)
# print(right.shape)