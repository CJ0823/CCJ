numbers = [2, 4, 6, 8, 10, 12, 14]

# 리스트 뒤집기
# 코드를 입력하세요.

for i in range(int(len(numbers) / 2)):
    right = len(numbers) - i - 1
    temp = numbers[i]
    numbers[i] = numbers[right]
    numbers[right] = temp
print("뒤집어진 리스트: " + str(numbers))