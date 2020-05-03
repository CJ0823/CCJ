#https://www.youtube.com/watch?v=UlyL5hY4Fd4(유튜브:OnLifeCoding)
import requests as req
import bs4
# pip install --user beautifulsoup4
# import bs4로 불러옴
# as req로 하면, 마치 약자로 단어를 쓰듯이 requests 모듈을 req로 불러올 수 있게 된다.
#읽어올 웹 페이지의 주소가 필요
url = "https://www.datacamp.com/tracks/data-scientist-with-python"
#웹 페이지의 내용을 읽어와야 한다
res = req.get(url)

#특정 요소만 검색하기
# 데이터를 분석하기 위해서 BeautifulSoup을 쓴다.
# .text는 따온 정보를 text화 시켜준다.
# 뒤쪽의 html.parser는 웹페이지라서, html 이라는 parser(문법분석)를 이용하겠다는 뜻임
bs = bs4.BeautifulSoup(res.text, features = "html.parser")

#bs를 이용해서 특정 selector를 선택한다.
# 원하는 웹페이지에서 개발자도구(F12)에 가서, 해당되는 곳의 elements를 찾고, 상위 class를 선택한다.
courses = bs.select(".css-10s95pl")
#courses = bs.select("#gatsby-focus-wrapper > div > div.container.css-93pq91 > div.col-md-8 > div > div > div > div.css-10s95pl > a")
# 결과를 한줄씩 출력하기 위해서 for문을 쓴다. 
# 특정 속성값을 불러오기 위해 attrs 라이브러리를 쓰고, 링크를 불러오기 위해서 링크를 갖는 tag인 href를 쓴다.
# select를 쓰면 list형태로 데이터를 갖고 오게 된다. 이 list는 text화 할 수 없으므로
# select_one을 이용하여 text화 한다.
# .getText() 는 class에 해당하는 정보 중, tag 정보는 제외하고 text로 된 부분만 가져오도록 해준다.
# .strip()은 text 중 빈곳을 제거할 수 있다... 실제 유용성은 추후 알아보기

courseList=[]
for i in courses:
    link = i.a.attrs["href"]
    title = i.select_one("h4").getText()
    desc = i.select_one("p").getText()
    courseList.append({'Link': link, 'title': title, 'desc': desc})
print(courseList)