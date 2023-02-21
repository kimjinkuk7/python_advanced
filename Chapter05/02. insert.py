# 모듈 추가
import sqlite3

# 데이터베이스 열기
conn = sqlite3.connect('myvenv/Chapter05/SQL_DDL.db')

# 커서 생성
cur = conn.cursor()

# SQL 명령 작성
INSERT_SQL = "insert into Item (code, name, price) values(?, ?, ?)"

# SQL 명령 싱행
# cur.execute(INSERT_SQL, ('A00001', '게이밍 마우스', 38000))

# 데이터 여러개 한번에 추가하기
data = (
    ('A0002', '에어컨 20평형', 350000),
    ('A0003', '최신형 스마트폰', 800000),
    ('A0004', '가성비 노트북', 650000)
)

cur.executemany(INSERT_SQL, data)

# commit : insert, update, delete는 commit을 해야 실제 데이터 반영이 된다.
conn.commit()

# 데이터베이스 닫기
conn.close()