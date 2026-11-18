import unittest

# Hàm tính tổng tiền dựa trên đơn giá và số lượng (logic của phần đặt món)
def tinh_tong_tien(don_gia, so_luong):
    return don_gia * so_luong

class TestOrderUI(unittest.TestCase):
    
    def test_tinh_tien_thanh_cong(self):
        # 1. Arrange (Chuẩn bị dữ liệu: Mì hải sản 55.000đ, mua 2 phần)
        don_gia = 55000
        so_luong = 2
        gia_tri_mong_doi = 110000

        # 2. Act (Thực thi hàm tính toán)
        ket_qua_thuc_te = tinh_tong_tien(don_gia, so_luong)

        # 3. Assert (Kiểm tra xem kết quả thực tế có khớp với mong đợi không)
        self.assertEqual(ket_qua_thuc_te, gia_tri_mong_doi)

if __name__ == '__main__':
    unittest.main()
    