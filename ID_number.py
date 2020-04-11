# 매출 파일 열기
# 파일 경로는 "data/chicken.txt" 입니다.
raw = open('data/chicken.txt','r', encoding = 'utf-8')

# 열린 파일을 string으로 만들기
string=''
for i in raw:
    string += i

# string을 '\n'기준으로 split
list=[]
list = string.split()
print(list)

#list에서 매출항만 추출
list_price=[]
for i in range(1,int(len(list)/2),2):
    list_price += list[i] 
print(list_price)

# 파일 닫기