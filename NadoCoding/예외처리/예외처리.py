try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요 :")))
    nums.append(int(input("첫번째 숫자를 입력하세요 :")))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:                                                  # 입력값을 정수가 아닌 것을 넣었을 때 ex)일, 이, 삼
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:                                    # 나누기에 0을 넣었을 때 ex) 6 / 0 ---> ZeroDivisionError
    print(err)                                                      # 해당하는 에러에 대한 프린트
except:
    print("알 수 없는 에러가 발생하였습니다.")

