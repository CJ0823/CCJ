<<<<<<< HEAD
# https://www.youtube.com/watch?v=3b_VMk3WlNY (유튜브: 프로그래머 김플 스튜디오)
#selenium을 설치한다. pip install selenium
#Chrome driver을 구글에서 다운로드 받아서, 압축을 풀고, exe파일을 실습파일이 있는 폴더에 넣어준다.
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

#구글에서 파이썬을 검색하면 복잡한 url이 뜨는데, 이미지, 동영상 등 탭들을 눌러보면 url에서 바뀌지 않는 부분이 있고,
#이 부분만 따서 검색을 해도 동일한 결과가 나옴을 알 수 있다.
baseUrl = 'https://www.google.com/search?q='
plusUrl = input('무엇을 검색할까요? :')
url = baseUrl + quote_plus(plusUrl)
#quote_plus는 한국어를 인코딩하여 변환된 코드로 나타내준다.

# webdriver는 브라우저를 제어하는 것이다.
# Chromedriver를 같은 폴더에 넣어놨으므로, 특별히 주소를 입력할 필요는 없다.
driver = webdriver.Chrome()
# url을 넣어서 검색을 하게 된다.
driver.get(url)

# page source들을 받아온다
html = driver.page_source
soup = BeautifulSoup(html)

# 구글 검색화면에서 개발자도구로 제목, 주소를 갖고 오기 위해서 검색을 해보면,
# class가 r인 tag에 제목 및 주소가 포함되어 있음을 알 수 있다. 아래와 같이 r class를 선택하여 불러온다
r = soup.select('.r')
# select를 쓰면 list형태로 데이터를 갖고 오게 된다. 이 list는 text화 할 수 없으므로
# select_one을 이용하여 text화 한다.
for i in r:
    print(i.select_one('.LC20lb').text)
    print(i.select_one('.iUh30').text)
    # class이름을 가져올때, Class 이름 내에 띄어쓰기가 있다면, 뒷부분은 삭제하면 된다. 이유는 다음에 알아보자...
    #빈줄 출력
    #주소 링크를 갖고 오기 위해서, 특정 태그의 속성을 가져오는 attrs를 쓴다.
    print(i.a.attrs['href'])
    print()
# 다 끝나면 driver를 닫아준다.
# 구글 페이지 같은 곳들은 검색결과가 계속해서 바뀌고, class 이름들이 자동으로 바뀌고, header값이 없으면 
# 접근을 막는 경우도 있으므로, 문제가 생기면 class 이름들이 바뀌었거나 접근이 막혔는지 알아봐야 한다.
=======
# https://www.youtube.com/watch?v=3b_VMk3WlNY (유튜브: 프로그래머 김플 스튜디오)
#selenium을 설치한다. pip install selenium
#Chrome driver을 구글에서 다운로드 받아서, 압축을 풀고, exe파일을 실습파일이 있는 폴더에 넣어준다.
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

#구글에서 파이썬을 검색하면 복잡한 url이 뜨는데, 이미지, 동영상 등 탭들을 눌러보면 url에서 바뀌지 않는 부분이 있고,
#이 부분만 따서 검색을 해도 동일한 결과가 나옴을 알 수 있다.
baseUrl = 'https://www.google.com/search?q='
plusUrl = input('무엇을 검색할까요? :')
url = baseUrl + quote_plus(plusUrl)
#quote_plus는 한국어를 인코딩하여 변환된 코드로 나타내준다.

# webdriver는 브라우저를 제어하는 것이다.
# Chromedriver를 같은 폴더에 넣어놨으므로, 특별히 주소를 입력할 필요는 없다.
driver = webdriver.Chrome()
# url을 넣어서 검색을 하게 된다.
driver.get(url)

# page source들을 받아온다
html = driver.page_source
soup = BeautifulSoup(html)

# 구글 검색화면에서 개발자도구로 제목, 주소를 갖고 오기 위해서 검색을 해보면,
# class가 r인 tag에 제목 및 주소가 포함되어 있음을 알 수 있다. 아래와 같이 r class를 선택하여 불러온다
r = soup.select('.r')
# select를 쓰면 list형태로 데이터를 갖고 오게 된다. 이 list는 text화 할 수 없으므로
# select_one을 이용하여 text화 한다.
for i in r:
    print(i.select_one('.LC20lb').text)
    print(i.select_one('.iUh30').text)
    # class이름을 가져올때, Class 이름 내에 띄어쓰기가 있다면, 뒷부분은 삭제하면 된다. 이유는 다음에 알아보자...
    #빈줄 출력
    #주소 링크를 갖고 오기 위해서, 특정 태그의 속성을 가져오는 attrs를 쓴다.
    print(i.a.attrs['href'])
    print()
# 다 끝나면 driver를 닫아준다.
# 구글 페이지 같은 곳들은 검색결과가 계속해서 바뀌고, class 이름들이 자동으로 바뀌고, header값이 없으면 
# 접근을 막는 경우도 있으므로, 문제가 생기면 class 이름들이 바뀌었거나 접근이 막혔는지 알아봐야 한다.
>>>>>>> 9522c36... first commit
driver.close()