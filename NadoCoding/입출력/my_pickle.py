# pickle 프로그램 상에서 사용하고 있는 데이터를 파일형태로 저장하는 것.
import pickle
# profile_file = open("profile.pickle", "wb") #wb---> 바이너리 타입,쓰기  pickle에서는 따로 인코딩 해줄필요 없음
# profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #(파일에 저장할 내용, 어떤파일에 쓸건지) profile에 있는 정보를 profile_file에 저장
# profile_file.close()


# pickle에 저장된 파일 불러오기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) #profile_file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close() 