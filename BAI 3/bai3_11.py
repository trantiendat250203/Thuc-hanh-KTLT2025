def benefit(t, n, k):
    for month in range(k):
        n += n * (t / 100)  
    return n
try:
    t = float(input("Nhập lãi suất tiết kiệm t (%/tháng): "))
    n = float(input("Nhập số vốn ban đầu n: "))
    k = int(input("Nhập số tháng gửi k: "))
    
    if n < 0 or k < 0:
        print("Số vốn và số tháng gửi phải là số dương.")
    else:
        final_amount = benefit(t, n, k)
        print(f"Số tiền nhận được sau {k} tháng là: {final_amount:.2f} VND")
except ValueError:
    print("Giá trị nhập vào không hợp lệ! Vui lòng nhập số.")
print ("sinh vien: Tran Van Tien Dat")
print ("Mssv: 235752020710004")