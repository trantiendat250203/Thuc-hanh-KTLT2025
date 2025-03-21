ds = input('Nhập chuỗi: ').split()
try:
    ds.remove('123')
except ValueError:
    print("'123' không có trong danh sách.")
for ch in ds:
    print(ch)
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")