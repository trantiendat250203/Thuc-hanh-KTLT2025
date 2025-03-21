ds = input('Nhập chuỗi: ').split()
try:
    position = ds.index('abc')
    print("Vị trí của chuỗi 'abc' là:", position)
except ValueError:
    print("'abc' không có trong danh sách.")
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")