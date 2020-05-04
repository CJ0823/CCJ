<<<<<<< HEAD
# crawling02_chromedriver
# 유튜브 https://www.youtube.com/watch?v=qjC83z7kJ0g
# 웹페이지에 클릭해도 주소가 바뀌지 않는 버튼이 있을 경우, 해당 버튼을 눌러 목록을 더 조회해야 할 때는 driver가 필요하다.

from selenium import webdriver
import bs4

#formatting 문법을 써서 base_url과 url을 합쳐준다.
base_url = "https://www.datacamp.com"
url = f"{base_url}/tracks/data-scientist-with-python"

# Chrome driver를 불러온다
driver = webdriver.Chrome()
# Driver 실행에 시간이 걸릴 수 있으니, 3초간 대기시간을 준다.
driver.implicitly_wait(3)
# driver가 url을 받아오도록 한다.
driver.get(url)
# 버튼을 xpath를 입력하여 찾아오고, btn 변수에 저장한다.
# 버튼이 간단한 경우에 xpath를 쓴다. 개발자도구에서 해당 버튼 위치를 find하고, html 코드에서 우클릭하여 Copy > Copy Xpath를 한다.
#() 안에 주석처리를 해야되는데, Xpath 자체에 주석문 ""가 있으므로 양끝에 "를 3개써서 주석처리해준다.
btn = driver.find_element_by_xpath("""//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[1]/div/div/div[4]/button""")
#btn을 클릭해준다.
btn.click()

#crawling01 파일의 내용을 가져와서 조금 수정해준다.

#웹 페이지의 내용을 읽어와야 한다
##res = req.get(url) : Driver를 사용하므로 request는 제외한다.

#특정 요소만 검색하기
# 데이터를 분석하기 위해서 BeautifulSoup을 쓴다.
# .text는 따온 정보를 text화 시켜준다.
# 뒤쪽의 html.parser는 웹페이지라서, html 이라는 parser(문법분석)를 이용하겠다는 뜻임
# 셀레니움을 이용하므로, driver에게 page source를 불러오라고 하면된다. res.text 대신 driver.page_source를 입력해준다,
bs = bs4.BeautifulSoup(driver.page_source, features = "html.parser")

#bs를 이용해서 특정 selector를 선택한다.
# 원하는 웹페이지에서 개발자도구(F12)에 가서, 해당되는 곳의 elements를 찾고, 상위 class를 선택한다.
courses = bs.select(".css-10s95pl")
#courses = bs.select("#gatsby-focus-wrapper > div > div.container.css-93pq91 > div.col-md-8 > div > div > div > div.css-10s95pl > a")
# 결과를 한줄씩 출력하기 위해서 for문을 쓴다. 
# 특정 속성값을 불러오기 위해 attrs 라이브러리를 쓰고, 링크를 불러오기 위해서 링크를 갖는 tag인 href를 쓴다.
# select를 쓰면 list형태로 데이터를 갖고 오게 된다. 이 list는 text화 할 수 없으므로
# select_one을 이용하여 text화 한다.
# .getText() 는 class에 해당하는 정보 중, tag 정보는 제외하고 text로 된 부분만 가져오도록 해준다.
# .strip()은 text 의 앞뒤에 있는 불필요한 공백을 지워준다.

courseList=[]
for i in courses:
    link = i.a.attrs["href"]
    title = i.select_one("h4").getText()
    desc = i.select_one("p").getText()
    courseList.append({'link': link, 'title': title, 'desc': desc})
print(courseList)

# Link를 가져오는 것을 보면, 기본이 되는 앞쪽 .com url은 가져오지 않음을 알 수 있다.
# 따라서 base_url을 지정해주고, 이것을 뒤쪽 link의 url과 함께 써서 활용하도록 한다.

# 해당 페이지에서 위 내용 외에 chapter 목록을 가져오기 위해서 아래와 같이 작성한다.
# variable c 뒤에 []를 써주고, ''안에 변수 link를 써주면... 차례대로 '주석문 link' 에 해당하는 내용만 반복하는 것 같다.

for c in courseList:
    # ""를 두개 써서 겹치는 일이 없도록 한다.
    driver.get(f"{base_url}{c['link']}")
    #불러온 주소를 bs를 이용하여 분석하겠다고 다시 정의한다.
    bs_detail = bs4.BeautifulSoup(driver.page_source, features = "html.parser")
    #chapter를 찾는다.
    #동일한 class 유형으로 여러개가 있다면, 첫번째 class(내용을 모두 포함하는 class)로 찾아야 한다.
    chapters = bs_detail.select_one("li.dc-chapter-block-card dc-card dc-card--shadowed-sm dc-u-mb-16 dc-u-p-none dc-u-fx@md dc-u-fx-fdc@md")
    # 하나씩 class를 내려간다.
    chapters_elem = chapters.select("div.dc-u-fxi-fg-1")

    chapter_list = []
    for chap in chapters_elem:
        chap_title = chap.select_one("h4.dc-u-ml-8 dc-u-mt-0").getText().strip()
        chap_desc = chap.select_one("div.dc-chapter-block-description dc-u-mb-24 dc-u-mt-0 dc-u-ph-16").getText().strip()
        chap_details_elem = chap.select("a.dc-chapter-block-link dc-u-fx dc-u-fx-aic dc-u-fx-jcsb dc-u-fw-bold dc-u-pv-8 dc-u-ph-16").getText().strip()

        chap_detail_titles = []
        for cd in chap_details_elem:
            cd_title = cd.getText().strip()
            chap_detail_titles.append(cd_title)

        chapter_detail = {"title" : chap_title, "desc":chap_desc, "details": chap_detail_titles}
        print(chapter_detail)
        chapter_list.append(chapter_detail)
=======
# crawling02_chromedriver
# 유튜브 https://www.youtube.com/watch?v=qjC83z7kJ0g
# 웹페이지에 클릭해도 주소가 바뀌지 않는 버튼이 있을 경우, 해당 버튼을 눌러 목록을 더 조회해야 할 때는 driver가 필요하다.

from selenium import webdriver
import bs4

#formatting 문법을 써서 base_url과 url을 합쳐준다.
base_url = "https://www.datacamp.com"
url = f"{base_url}/tracks/data-scientist-with-python"

# Chrome driver를 불러온다
driver = webdriver.Chrome()
# Driver 실행에 시간이 걸릴 수 있으니, 3초간 대기시간을 준다.
driver.implicitly_wait(3)
# driver가 url을 받아오도록 한다.
driver.get(url)
# 버튼을 xpath를 입력하여 찾아오고, btn 변수에 저장한다.
# 버튼이 간단한 경우에 xpath를 쓴다. 개발자도구에서 해당 버튼 위치를 find하고, html 코드에서 우클릭하여 Copy > Copy Xpath를 한다.
#() 안에 주석처리를 해야되는데, Xpath 자체에 주석문 ""가 있으므로 양끝에 "를 3개써서 주석처리해준다.
btn = driver.find_element_by_xpath("""//*[@id="gatsby-focus-wrapper"]/div/div[1]/div[1]/div/div/div[4]/button""")
#btn을 클릭해준다.
btn.click()

#crawling01 파일의 내용을 가져와서 조금 수정해준다.

#웹 페이지의 내용을 읽어와야 한다
##res = req.get(url) : Driver를 사용하므로 request는 제외한다.

#특정 요소만 검색하기
# 데이터를 분석하기 위해서 BeautifulSoup을 쓴다.
# .text는 따온 정보를 text화 시켜준다.
# 뒤쪽의 html.parser는 웹페이지라서, html 이라는 parser(문법분석)를 이용하겠다는 뜻임
# 셀레니움을 이용하므로, driver에게 page source를 불러오라고 하면된다. res.text 대신 driver.page_source를 입력해준다,
bs = bs4.BeautifulSoup(driver.page_source, features = "html.parser")

#bs를 이용해서 특정 selector를 선택한다.
# 원하는 웹페이지에서 개발자도구(F12)에 가서, 해당되는 곳의 elements를 찾고, 상위 class를 선택한다.
courses = bs.select(".css-10s95pl")
#courses = bs.select("#gatsby-focus-wrapper > div > div.container.css-93pq91 > div.col-md-8 > div > div > div > div.css-10s95pl > a")
# 결과를 한줄씩 출력하기 위해서 for문을 쓴다. 
# 특정 속성값을 불러오기 위해 attrs 라이브러리를 쓰고, 링크를 불러오기 위해서 링크를 갖는 tag인 href를 쓴다.
# select를 쓰면 list형태로 데이터를 갖고 오게 된다. 이 list는 text화 할 수 없으므로
# select_one을 이용하여 text화 한다.
# .getText() 는 class에 해당하는 정보 중, tag 정보는 제외하고 text로 된 부분만 가져오도록 해준다.
# .strip()은 text 의 앞뒤에 있는 불필요한 공백을 지워준다.

courseList=[]
for i in courses:
    link = i.a.attrs["href"]
    title = i.select_one("h4").getText()
    desc = i.select_one("p").getText()
    courseList.append({'link': link, 'title': title, 'desc': desc})
print(courseList)

# Link를 가져오는 것을 보면, 기본이 되는 앞쪽 .com url은 가져오지 않음을 알 수 있다.
# 따라서 base_url을 지정해주고, 이것을 뒤쪽 link의 url과 함께 써서 활용하도록 한다.

# 해당 페이지에서 위 내용 외에 chapter 목록을 가져오기 위해서 아래와 같이 작성한다.
# variable c 뒤에 []를 써주고, ''안에 변수 link를 써주면... 차례대로 '주석문 link' 에 해당하는 내용만 반복하는 것 같다.

for c in courseList:
    # ""를 두개 써서 겹치는 일이 없도록 한다.
    driver.get(f"{base_url}{c['link']}")
    #불러온 주소를 bs를 이용하여 분석하겠다고 다시 정의한다.
    bs_detail = bs4.BeautifulSoup(driver.page_source, features = "html.parser")
    #chapter를 찾는다.
    #동일한 class 유형으로 여러개가 있다면, 첫번째 class(내용을 모두 포함하는 class)로 찾아야 한다.
    chapters = bs_detail.select_one("li.dc-chapter-block-card dc-card dc-card--shadowed-sm dc-u-mb-16 dc-u-p-none dc-u-fx@md dc-u-fx-fdc@md")
    # 하나씩 class를 내려간다.
    chapters_elem = chapters.select("div.dc-u-fxi-fg-1")

    chapter_list = []
    for chap in chapters_elem:
        chap_title = chap.select_one("h4.dc-u-ml-8 dc-u-mt-0").getText().strip()
        chap_desc = chap.select_one("div.dc-chapter-block-description dc-u-mb-24 dc-u-mt-0 dc-u-ph-16").getText().strip()
        chap_details_elem = chap.select("a.dc-chapter-block-link dc-u-fx dc-u-fx-aic dc-u-fx-jcsb dc-u-fw-bold dc-u-pv-8 dc-u-ph-16").getText().strip()

        chap_detail_titles = []
        for cd in chap_details_elem:
            cd_title = cd.getText().strip()
            chap_detail_titles.append(cd_title)

        chapter_detail = {"title" : chap_title, "desc":chap_desc, "details": chap_detail_titles}
        print(chapter_detail)
        chapter_list.append(chapter_detail)
>>>>>>> 9522c36... first commit
    break