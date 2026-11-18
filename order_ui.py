# Chương trình đặt món Mì Cay đơn giản dành cho người mới học Python

def dat_mon():
    print("=== CHƯƠNG TRÌNH ĐẶT MÓN MÌ CAY ===")
    
    # 1. Chọn món ăn
    print("\nDanh sách món mì cay:")
    print("1. Mì Cay Hải Sản (55.000đ)")
    print("2. Mì Cay Bò Mỹ (52.000đ)")
    print("3. Mì Cay Thập Cẩm (65.000đ)")
    
    chon_mon = input("Nhập lựa chọn của bạn (1-3): ")
    
    if chon_mon == "1":
        ten_mon = "Mì Cay Hải Sản"
        gia = 55000
    elif chon_mon == "2":
        ten_mon = "Mì Cay Bò Mỹ"
        gia = 52000
    elif chon_mon == "3":
        ten_mon = "Mì Cay Thập Cẩm"
        gia = 65000
    else:
        print("Lựa chọn không hợp lệ! Mặc định chọn Mì Cay Hải Sản.")
        ten_mon = "Mì Cay Hải Sản"
        gia = 55000

    # 2. Chọn cấp độ cay (0 - 7)
    print("\n--- TÙY CHỌN CẤP ĐỘ CAY ---")
    print("Từ Level 0 (Không cay) đến Level 7 (Thử thách)")
    
    try:
        level_cay = int(input("Nhập cấp độ cay bạn muốn (0 đến 7): "))
        if level_cay < 0 or level_cay > 7:
            print("Cấp độ không hợp lệ, hệ thống sẽ mặc định để Level 0.")
            level_cay = 0
    except ValueError:
        print("Bạn phải nhập số! Hệ thống sẽ mặc định để Level 0.")
        level_cay = 0

    # 3. Nhập số lượng
    try:
        so_luong = int(input("\nNhập số lượng phần: "))
        if so_luong < 1:
            so_luong = 1
    except ValueError:
        so_luong = 1

    # 4. Tính tổng tiền và in hóa đơn
    tong_tien = gia * so_luong

    print("\n" + "="*30)
    print("📋 XÁC NHẬN ĐƠN HÀNG CỦA BẠN:")
    print(f"- Món: {ten_mon}")
    print(f"- Cấp độ cay: Level {level_cay}")
    print(f"- Số lượng: {so_luong}")
    print(f"- Tổng tiền thanh toán: {tong_tien:,}đ")
    print("="*30)

# Chạy chương trình
if __name__ == "__main__":
    dat_mon()