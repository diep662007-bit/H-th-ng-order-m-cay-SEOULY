class FoodOrderService:
    """Service xử lý gọi món, tính tiền kèm phụ phí cấp độ cay."""
    def calculate_order_total(self, base_price: float, quantity: int, spice_level: int) -> float:
        if quantity <= 0 or base_price < 0:
            return 0.0
        
        subtotal = base_price * quantity
        # Nếu cấp độ cay từ 3 trở lên, phụ phí thêm 5.000đ mỗi phần
        if spice_level >= 3:
            subtotal += 5000 * quantity
            
        return subtotal