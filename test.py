import unittest
from order_service import OrderService

class TestOrderService(unittest.TestCase):

    def test_add_available_dish_success(self):
        # 1. Arrange (Chuẩn bị dữ liệu)
        service = OrderService()
        product = {"id": "P01", "name": "Mì Kim Chi Hải Sản", "price": 49000, "is_available": True}
        
        # 2. Act (Thực thi hành động)
        result = service.add_dish_to_order(product, spice_level=3, quantity=2)
        
        # 3. Assert (Kiểm tra kết quả mong đợi)
        self.assertIn("Thành công", result)
        self.assertEqual(len(service.get_order_details()), 1)

    def test_add_out_of_stock_dish(self):
        # 1. Arrange
        service = OrderService()
        product = {"id": "P02", "name": "Mì Kim Chi Bò Mỹ", "price": 52000, "is_available": False}
        
        # 2. Act
        result = service.add_dish_to_order(product, spice_level=2, quantity=1)
        
        # 3. Assert
        self.assertIn("Lỗi", result)
        self.assertIn("HẾT", result)
        self.assertEqual(len(service.get_order_details()), 0)

    def test_invalid_spice_level(self):
        # 1. Arrange
        service = OrderService()
        product = {"id": "P01", "name": "Mì Kim Chi Hải Sản", "price": 49000, "is_available": True}
        
        # 2. Act (Cấp độ 9 vượt quá ngưỡng cho phép 0-7)
        result = service.add_dish_to_order(product, spice_level=9, quantity=1)
        
        # 3. Assert
        self.assertIn("Lỗi", result)
        self.assertIn("Cấp độ cay", result)
        self.assertEqual(len(service.get_order_details()), 0)

if __name__ == '__main__':
    unittest.main()