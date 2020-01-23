# open_dart
전자공시 Open Dart 분석 및 관련 자료 정리

2020-01-21 부터 시범 서비스 중인 전자공시 Open API 사용 방법에 대한 연구

# 완전 뉴비를 위한 API 설명
1. 각 개발가이드 설명에 있는 '상세주소'를 요청 하면 거기 맞는 응답을 준다.
## 좀 더 자세한 설명
1. 인증키를 먼저 받는다.
1. '상세주소'에 요청 인자를 넣는다. URL과 요청인자 사이는 '?' 로 연결하고, 각 인자는 '&'으로 연결해 여러 인자를 넘겨줄 수 있다.
1. 각 인자에 값 지정은 '='로 한다.
   1. 예제: 삼성전자 사업연도 2019년 1분기 재무정보 조회 (crtfc_key 항목은 자신의 키를 넣어야 함.)
   ```
   https://opendart.fss.or.kr/api/fnlttSinglAcnt.json?crtfc_key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&corp_code=00126380&bsns_year=2019&reprt_code=110113
   ```
1. 종목코드(stock_code. HTS, MTS 등에서 사용하는)와 Open API에서 사용하는 회사 코드 (corp_code)는 다르다. 처음에 고유번호부터 확보해야 한다.
   1. 비상장 회사 등의 중요사항 공시에 관한 규정이 있다. 
   1. 종목코드 없는 비상장사 정보조회하려면 당연.
   1. https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx 로 요청하면 Zip으로 압축된 xml 파일을 다운로드 가능.
1. xml 혹은 json으로 요청하면 해당 포멧 혹은 파일을 받을 수 있음.
