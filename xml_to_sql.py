import pandas as pd
import xml.etree.ElementTree as ET
import sys
from urllib.request import urlopen
import sqlite3

CONN = sqlite3.connect("db/code.db")

# open dart corp_code.zip 파일 다운로드 하고 자체 웹 데몬에서 접근 가능한 경우
url = "https://localhost/CORPCODE.xml"

response = urlopen(url).read()
xtree = ET.fromstring(response)

df_cols = ["corp_code", "corp_name", "stock_code", "modify_date"]
rows = []

for node in xtree: 
    s_corp_code = node.find("corp_code").text if node is not None else None
    s_corp_name = node.find("corp_name").text if node is not None else None
    s_stock_code = node.find("stock_code").text if node is not None else None
    s_modify_date = node.find("modify_date").text if node is not None else None
    
    rows.append({"corp_code": s_corp_code, "corp_name": s_corp_name, 
                 "stock_code": s_stock_code, "modify_date": s_modify_date})

out_df = pd.DataFrame(rows, columns = df_cols)

out_df.to_sql('code', CONN)
# out_df.to_csv('code.csv')