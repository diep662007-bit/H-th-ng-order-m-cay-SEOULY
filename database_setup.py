import sqlite3

def init_database(db_name="micay_seouly.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    # Bật ràng buộc khóa ngoại trong SQLite
    cursor.execute("PRAGMA foreign_keys = ON;")

    # 1. Tạo bảng SpiceLevels (cấp độ cay từ 0-7)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS SpiceLevels (
        SpiceLevelID INTEGER PRIMARY KEY,
        LevelName TEXT NOT NULL,
        Description TEXT,
        CONSTRAINT CHK_SpiceLevel_Range CHECK (SpiceLevelID BETWEEN 0 AND 7)
    );
    """)

    # 2. Tạo bảng Products (món ăn)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Products (
        ProductID INTEGER PRIMARY KEY AUTOINCREMENT,
        ProductName TEXT NOT NULL,
        Price REAL NOT NULL CHECK (Price >= 0),
        Category TEXT,
        IsAvailable INTEGER DEFAULT 1,
        DefaultSpiceLevelID INTEGER NULL,
        FOREIGN KEY (DefaultSpiceLevelID) REFERENCES SpiceLevels(SpiceLevelID)
    );
    """)

    # Thêm dữ liệu mặc định cho 8 cấp độ cay (0 - 7)
    spice_data = [
        (0, 'Cấp độ 0', 'Không cay'),
        (1, 'Cấp độ 1', 'Cay nhẹ'),
        (2, 'Cấp độ 2', 'Cay vừa'),
        (3, 'Cấp độ 3', 'Cay nồng'),
        (4, 'Cấp độ 4', 'Rất cay'),
        (5, 'Cấp độ 5', 'Siêu cay'),
        (6, 'Cấp độ 6', 'Cực đại'),
        (7, 'Cấp độ 7', 'Bùng nổ')
    ]
    cursor.executemany(
        "INSERT OR IGNORE INTO SpiceLevels (SpiceLevelID, LevelName, Description) VALUES (?, ?, ?);", 
        spice_data
    )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_database()
    print("Khoi tao CSDL Products va SpiceLevels thanh cong!")