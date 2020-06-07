"""Divide and Conquer 방식으로 merge_sort 함수를 써 보세요. merge_sort는 파라미터로 리스트 하나를 받고, 정렬된 새로운 리스트를 리턴합니다.


merge 함수는 이전 과제에서 작성한 그대로 사용하면 됩니다!"""

def merge(list1, list2):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    merged_list = []
    while list1 != [] or list2 != []:
        if list1 == []:
            merged_list.append(list2[0])
            list2.remove(list2[0])
        elif list2 == []:
            merged_list.append(list1[0])
            list1.remove(list1[0])
        elif list1[0] <= list2[0]:
            merged_list.append(list1[0])
            list1.remove(list1[0])
        else:
            merged_list.append(list2[0])
            list2.remove(list2[0])
    return merged_list
    
# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
    if len(my_list) == 1:
        return merge(my_list, [])
    list1 = my_list[:len(my_list)//2]
    list2 = my_list[len(my_list)//2:]
    return merge(merge_sort(list1),merge_sort(list2))

# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
