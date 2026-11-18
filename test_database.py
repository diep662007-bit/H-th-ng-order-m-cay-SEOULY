import unittest
import sqlite3
import os
from database_setup import init_database

class TestDatabaseSetup(unittest.TestCase):
    def setUp(self):
        # Arrange: Tạo file CSDL tạm để kiểm thử
        self.test_db = "test_micay_temp.db"
        init_database(self.test_db)
        self.conn = sqlite3.connect(self.test_db)
        self.cursor = self.conn.cursor()
        self.cursor.execute("PRAGMA foreign_keys = ON;")

    def tearDown(self):
        # Dọn dẹp: Đóng kết nối và xóa file CSDL tạm sau khi chạy test xong
        self.conn.close()
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_spice_levels_count(self):
        # Arrange: Đã khởi tạo 8 cấp độ cay ở setUp
        # Act: Truy vấn đếm số lượng cấp độ cay trong bảng SpiceLevels
        self.cursor.execute("SELECT COUNT(*) FROM SpiceLevels;")
        count = self.cursor.fetchone()[0]
        
        # Assert: Phải có đúng 8 cấp độ (từ 0 đến 7)
        self.assertEqual(count, 8, "Bang SpiceLevels phai co du 8 cap do cay tu 0-7")

    def test_invalid_spice_level_constraint(self):
        # Arrange: Chuẩn bị dữ liệu cấp độ cay sai quy định (cấp 8)
        # Act & Assert: Hệ thống phải chặn lại và báo lỗi IntegrityError
        with self.assertRaises(sqlite3.IntegrityError):
            self.cursor.execute(
                "INSERT INTO SpiceLevels (SpiceLevelID, LevelName) VALUES (8, 'Cấp độ 8');"
            )

    def test_insert_product_valid(self):
        # Arrange: Dữ liệu món ăn hợp lệ với cấp độ cay 3
        # Act: Thêm món ăn vào bảng Products và truy vấn lại
        self.cursor.execute(
            "INSERT INTO Products (ProductName, Price, Category, DefaultSpiceLevelID) VALUES ('Mì cay Bò Mỹ', 59000, 'Mì cay', 3);"
        )
        self.cursor.execute("SELECT ProductName, Price FROM Products WHERE ProductName = 'Mì cay Bò Mỹ';")
        row = self.cursor.fetchone()

        # Assert: Dữ liệu lưu đúng tên và giá tiền
        self.assertIsNotNone(row)
        self.assertEqual(row[0], 'Mì cay Bò Mỹ')
        self.assertEqual(row[1], 59000)

if __name__ == '__main__':
    unittest.main()