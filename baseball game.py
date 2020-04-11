from random import randint
i=0
k=0
random_num=[0, 0, 0]
while i < 3:
    random_num[i] = randint(1,9)
    while random_num[i] == random_num[i-1] or random_num[i] == random_num[i-2]:
        random_num[i] = randint(1, 9)
    i += 1

print("0과 9 사이의 서로 다른 세 숫자를 랜덤한 순서로 뽑았습니다.")
print("세 수를 하나씩 차례대로 입력하세요.")
num1 = 0
num2 = 0
num3 = 0
num_S=0
num_B=0
user=[0, 0, 0]
user_try=0
while num_S != 3:
    user_try += 1
    num1 = int(input("1번째 수를 입력하세요: "))
    while num1 < 1 or num1 > 9:
        num1 = int(input("1번째 수를 입력하세요: "))
    num2 = int(input("2번째 수를 입력하세요: "))
    while num2 == num1 or num2 < 1 or num2 > 9:
        num2 = int(input("2번째 수를 입력하세요: "))
    num3 = int(input("3번째 수를 입력하세요: "))
    while num3 == num2 or num3 == num1 or num3 < 1 or num3 > 9:
        num3 = int(input("3번째 수를 입력하세요: "))
    user = [num1, num2, num3]
    if user[0] == random_num[0]:
        num_S += 1
    elif user[0] == random_num[1] or user[0] == random_num[2]:
        num_B += 1
    if user[1] == random_num[1]:
        num_S += 1
    elif user[1] == random_num[0] or user[1] == random_num[2]:
        num_B += 1
    if user[2] == random_num[2]:
        num_S += 1
    elif user[2] == random_num[0] or user[2] == random_num[1]:
        num_B += 1
    print("{}S {}B".format(num_S, num_B))
    if num_S == 3:
        print("축하합니다. {}번 만에 세 숫자의 값과 위치를 모두 맞추셨습니다.".format(user_try))
        break
    num_S = 0
    num_B = 0
    ### e다다다다