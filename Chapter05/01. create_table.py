# 모듈 추가
import sqlite3

# 데이터베이스 열기
conn = sqlite3.connect('myvenv/Chapter05/SQL_DDL.db')

# 커서 생성
cur = conn.cursor()

# SQL 명령 작성
CREATE_SQL = """
    CREATE TABLE IF NOT EXISTS Item(
        idx	INTEGER PRIMARY KEY AUTOINCREMENT,
        code	TEXT NOT NULL,
        name	TEXT NOT NULL,
        price	INTEGER NOT NULL
    )
"""

# SQL 명령 싱행
cur.execute(CREATE_SQL)

# 데이터베이스 닫기
conn.close()