# 외장함수는 직접 import해서 사용해야하는 것
# 'list of python modules' 검색 -> python module index

# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py 인 모든 파일

# ==============================================================================

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리를 표시해달라는 내용

# folder = "sample_dir"

# if os.path.exists(folder): # sample_dir이라는 폴더가 있으면 아래의 이 구문을 타라
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())

# ==============================================================================

# time : 시간 관련 함수
# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 뒤 저장
print("우리가 만난지 100일은", today + td) # 오늘부터 100일 후
