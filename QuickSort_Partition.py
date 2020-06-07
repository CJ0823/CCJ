"""Divide and Conquer 방식으로 quicksort 함수를 써 보세요. quicksort는 파라미터로 리스트 하나와 리스트 내에서 정렬시킬 범위를 나타내는 인덱스 start와 인덱스 end를 받습니다.
merge_sort 함수와 달리 quicksort 함수는 정렬된 새로운 리스트를 리턴하는 게 아니라, 파라미터로 받는 리스트 자체를 정렬시키는 것입니다.
swap_elements와 partition 함수는 이전 과제에서 작성한 그대로 사용하면 됩니다!
"""

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
    return my_list

# 퀵 정렬
def quicksort(my_list, start, end):
    # 코드를 작성하세요.
    if len(my_list) == 1:
        return my_list
    left = my_list[:len(my_list)//2]
    right = my_list[len(my_list)//2:]
    return partition(quicksort(left, 0, len(left)-1) + quicksort(right, 0, len(right)-1)

# 테스트 1
list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

# 테스트 2
list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)

# 테스트 3
list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
quicksort(list3, 0, len(list3) - 1)
print(list3)
