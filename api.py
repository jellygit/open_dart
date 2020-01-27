#!/bin/env python
import os
import json
from urllib.request import urlopen
import pandas as pd
from pandas.io.json import json_normalize
# API request to the URL
import sys

# 쉘 환경변수 DART_KEY 를 읽어온다.
# 리눅스에서 테스트. 윈도는 되는지 모르겠음.
API_KEY = os.environ["DART_KEY"]

# 배당 정보 가져오기
OPEN_DART = 'https://opendart.fss.or.kr/api/alotMatter.json?crtfc_key='+ API_KEY +'&corp_code=00163682&bsns_year=2019&reprt_code=11013'

response = urlopen(OPEN_DART)
json_data = response.read().decode('utf-8', 'replace')

d = json.loads(json_data)
df = json_normalize(d['list'])

print (df)