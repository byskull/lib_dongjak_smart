
 스마트도서관 - 이수점 도서목록 가져오기
============

동작구 통합 도서관 내 스마트 도서관
http://lib.dongjak.go.kr/dj/index.do?getContextPath=&isMobile=false

-------------

1. 싸이트에서 데이터 가져오기

# 처음에는 http://210.99.187.108:8088/EZ-950SL_Web/mainPage/SI_searchbookindex_Service.jsp 에서
# 바로 데이터를 가져와 봤습니다. 

```
browser.find_element_by_xpath("//a[contains(@onclick,\"PageMove('%i')\")]"%i).click()
```

# 이 방식을 통해서 페이지를 넘겨가며 데이터를 가져왔지만 (10페이지가 넘어가면 img에서 가져와야 함) 
# 문제는 처음 화면에서 스마트도서관(대방)과 이수점을 구분해서 가져와야 한다는 파라미터가 따로 있었습니다.

# 그래서 이 세줄이 추가 됩니다.

```
browser.get('http://210.99.187.108:8088/EZ-950SL_Web/mainPage/SI_searchbookindex.jsp')
Select(browser.find_element_by_name('no')).select_by_value("2")
browser.find_element_by_xpath("//img[contains(@onclick,\"SearchALL()\")]").click()
```

# select 로 콤보박스를 선택하고 밑에 버튼을 눌러줍니다.



2. txt file을 csv 파일로

# txt 파일을 저장할 때 바로 csv 파일로 저장 하면 안 될 이유가 없습니다만, 단 한가지 이유 때문에 그렇게 안 했습니다
# python 2.7 에서는 euc_kr 를 이용해서 출력하다보면 편집이 안 됩니다. 읽은 거에서 s + " " 를 했을 뿐인데
# \xa0를 읽을 수 없다는 메시지가 떠서, 그냥 저장하고 다시 읽어서 csv로 다시 쓰는 무식한 해법을 사용했습니다.
# 보면 csv 형식에 어울리지 않게 서로 컬럼 순서가 안 맞는 경우가 있는데요, 그냥 대출가능 여부만 앞으로 빼고 (엑셀에서 필터링 하려고)
# 나머지는 그냥 뒤에 덧붙이는 식으로 해결했습니다.
# 이걸 깔끔하게 해결하기 위해서는 웹서핑과, 탭 내용 분석이 필요한데 들이는 시간 대비 별 효과가 없을 것 같아서요.
