from food_order_service import FoodOrderService
import unittest

class TestFoodOrderService(unittest.TestCase):
    
    def test_normal_order(self):
        # 1. Arrange (Chuẩn bị dữ liệu và đối tượng)
        service = FoodOrderService()
        base_price = 30000.0
        quantity = 2
        spice_level = 1  # Cấp độ thấp (<3), không có phụ phí cay
        expected = 60000.0  # 30000 * 2
        
        # 2. Act (Thực thi phương thức cần kiểm thử)
        actual = service.calculate_order_total(base_price, quantity, spice_level)
        
        # 3. Assert (So sánh kết quả thực tế với mong đợi)
        self.assertEqual(expected, actual)

    def test_spicy_order(self):
        # 1. Arrange (Chuẩn bị dữ liệu)
        service = FoodOrderService()
        base_price = 40000.0
        quantity = 1
        spice_level = 3  # Cấp độ cay (>=3), cộng thêm 5000đ phụ phí
        expected = 45000.0  # (40000 * 1) + (5000 * 1)
        
        # 2. Act (Thực thi)
        actual = service.calculate_order_total(base_price, quantity, spice_level)
        
        # 3. Assert (Kiểm tra kết quả)
        self.assertEqual(expected, actual)

    def test_invalid_order_quantity(self):
        # 1. Arrange (Chuẩn bị dữ liệu với số lượng không hợp lệ)
        service = FoodOrderService()
        base_price = 35000.0
        quantity = 0  # Số lượng <= 0
        spice_level = 2
        expected = 0.0
        
        # 2. Act (Thực thi)
        actual = service.calculate_order_total(base_price, quantity, spice_level)
        
        # 3. Assert (Kiểm tra kết quả)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()