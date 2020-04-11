def binary_search(element, some_list):
    # 코드를 작성하세요.
    some_list.sort()
    index = len(some_list) // 2
    index_half = len(some_list) // 2
    while True:

        if some_list[index_half] < element:
            some_list = some_list[index_half:len(some_list)]
            index_half = len(some_list) // 2
            index += index_half
            if index == 0 and some_list[index_half] == element:
                return index
            elif inde:
                return None
        elif some_list[index_half] > element:
            some_list = some_list[:index_half]
            index_half = len(some_list) // 2
            index -= index_half
            if some_list[index_half] == element:
                return index
            else:
                return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))