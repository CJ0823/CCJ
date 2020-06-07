"""partition 함수 설명 영상을 토대로 partition 함수를 작성하세요.
partition 함수는 리스트 my_list, 그리고 partition할 범위를 나타내는 인덱스 start와 인덱스 end를 파라미터로 받습니다. 
my_list의 값들을 pivot 기준으로 재배치한 후, pivot의 최종 위치 인덱스를 리턴해야 합니다."""

"""partition 함수를 작성하다 보면 코드가 꽤나 지저분해질 수 있습니다. 
특히 리스트에서 값들의 위치를 바꿔주는 경우가 많은데요. 
코드가 지저분해지는 걸 방지하기 위해서 swap_elements라는 함수를 먼저 작성하겠습니다."""

# 두 요소의 위치를 바꿔주는 helper function
def swap_elements(my_list, index1, index2):
    # 코드를 작성하세요.
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

# 퀵 정렬에서 사용되는 partition 함수
def partition(my_list, start, end):
    # 코드를 작성하세요.
    pivot = my_list[end]
    b=0
    for i in range(len(my_list)):
        if my_list[i] < pivot:
            swap_elements(my_list, b, i)
            b += 1
    swap_elements(my_list, b, my_list.index(pivot))
    return my_list.index(pivot)

# 테스트 1
list1 = [4, 3, 6, 2, 7, 1, 5]
pivot_index1 = partition(list1, 0, len(list1) - 1)
print(list1)
print(pivot_index1)

# 테스트 2
list2 = [6, 1, 2, 6, 3, 5, 4]
pivot_index2 = partition(list2, 0, len(list2) - 1)
print(list2)
print(pivot_index2)

# 파이썬에서 가능한 더 간단한 스왑 방법 a, b= b, a
"""def swap_elements(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]"""
