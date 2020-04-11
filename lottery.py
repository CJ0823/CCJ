from random import randint
#무작위로 1과 45 사이의 서로 다른 여섯 개의 숫자를 뽑고, 오름차순으로 정렬되어있는 리스트를 리턴함.
#list1은 사용자가 뽑은 숫자 리스트, list2는 당첨번호 리스트가 됨.
def generate_numbers():
    list1 = []
    for i in range(6):
        num_user = randint(1,45)
        while num_user in list1:
            num_user = randint(1,45)
        list1.append(num_user)
    list1.sort()
    return list1

##generate_numbers 함수를 이용하여 당첨번호 6개에 보너스 번호를 포함시킨 리스트를 리턴시킴
def draw_winning_numbers():
    list2 = generate_numbers()
    bonus_num = randint(1,45)
    while bonus_num in list2:
        bonus_num = randint(1,45)
    list2.append(bonus_num)
    return list2

#list1과 list2를 파라미터로 받고, 두 리스트 간의 같은 숫자의 개수를 리턴시켜 준다.
def count_matching_numbers(list1, list2):
    count = 0
    for num_user in list1:
        if num_user in list2[:5]:
            count += 1
    return count

#user의 번호 6개가 있는 리스트 numbers와 당첨 번호가 있는 리스트 winning_numbers를 파라미터로 받고,
#규칙에 따라 당첨 금액을 리턴시켜 줌
def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers)
    prize = 0
    if count == 6:
        prize = 1000000000
    elif count == 5 and winning_numbers[6] in numbers:
        prize = 50000000
    elif count == 5:
        prize = 10000000
    elif count == 4:
        prize = 50000
    elif count == 3:
        prize = 5000
    return prize