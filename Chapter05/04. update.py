# 모듈 추가
import sqlite3

# 데이터베이스 열기
conn = sqlite3.connect('myvenv/Chapter05/SQL_DDL.db')

# 커서 생성
cur = conn.cursor()

# SQL 명령 작성
UPDATE_SQL = "UPDATE ITEM SET PRICE = 650000 WHERE CODE = 'A0002'"

# 명령어 실행
cur.execute(UPDATE_SQL)

conn.commit()

# 데이터베이스 닫기
conn.close()