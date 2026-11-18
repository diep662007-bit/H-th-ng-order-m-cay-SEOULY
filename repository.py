# Ví dụ mã nguồn Entity và Repository cho Quản lý Mì Cay
class Product:
    def __init__(self, id, name, price, spice_level):
        self.id = id
        self.name = name
        self.price = price
        self.spice_level = spice_level  # Cấp độ cay (0 - 7)

class ProductRepository:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"Đã thêm món: {product.name} thành công!")