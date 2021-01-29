import pickle

# with ----> 기존에 파일을 처리할때 파일을 열고 닫는것 까지 했으나, with를 쓰면 좀 더 편하게 동일한 작업이 가능.
# with open("profile.pickle", "rb") as profile_file:
# 	print(pickle.load(profile_file))
# close 필요없이 자동으로 종료

# with open("study.txt", "w", encoding="utf8") as study_file:
# 	study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
	print(study_file.read())