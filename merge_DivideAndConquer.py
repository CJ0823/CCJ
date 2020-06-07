"""합병 정렬 알고리즘 중 사용되는 merge 함수를 작성해 보세요.
merge 함수는 정렬된 두 리스트 list1과 list2를 받아서, 하나의 정렬된 리스트를 리턴합니다."""

def merge(list1, list2):
    # 코드를 작성하세요.
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
# 테스트
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))

## val = list.sort() 로 지정해버리면, val은 list를 정렬한 list가 되지 않는다.
## sort는 method 일뿐, 어떤 list를 정렬해서 다른 변수 list를 만들어주는 역할을 하는 것이 아니다.

# empty list의 index를 [0]번으로 불러와서 int로서 비교하는 것이 불가능해서 if문 2개를 추가하였음.
# 이것에 대한 해결책이 필요함.

""">>>우선 비어있는 리스트를 체크할 때 = []보다는 len()을 이용해서 길이가 0인지 확인하는게 더 좋다 생각해요. = []라고 적으면 다른 리스트랑 비교하는 게 될 수도 있어요!
그리고 비어있는 리스트는 당연하게도 인덱스 접근에서 오류가 납니다. 조건을 조금 더 세분화 시켜주세요!"""
#Codeit Cheezzz님의 답변