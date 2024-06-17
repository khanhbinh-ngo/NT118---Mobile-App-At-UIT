import sqlite3

conn = sqlite3.connect("qlsv.db")
c = conn.cursor()

# Tạo bảng
c.execute('''CREATE TABLE qlsv (
                MSSV TEXT PRIMARY KEY,
                HOTEN TEXT,
                LOP TEXT
            )''')

# Thêm dữ liệu mẫu
c.execute("INSERT INTO qlsv VALUES ('21520637', 'NGO VU KHANH BINH', 'MMTT2021')")
c.execute("INSERT INTO qlsv VALUES ('B21DCCN002', 'Tran Thi B', 'D21CQCN02-B')")

conn.commit()
conn.close()
