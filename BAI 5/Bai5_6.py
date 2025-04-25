# main.py
print("Đậu Văn Quốc Bảo")
print("MSSV:235752020710014")
import mymodule

# Nhập số lượng phần tử của danh sách
n = int(input("Nhập số lượng phần tử của danh sách: "))

# Nhập giá trị các phần tử của danh sách
lst = []
for i in range(n):
    value = float(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)

# Sử dụng các hàm từ module mymodule
max_value = mymodule.find_max(lst)
min_value = mymodule.find_min(lst)
sorted_list = mymodule.sort_list(lst)

# Tìm vị trí của phần tử lớn nhất và nhỏ nhất
max_index = mymodule.find_max_index(lst)
min_index = mymodule.find_min_index(lst)

# In kết quả
print(f"Phần tử lớn nhất trong danh sách: {max_value}, Vị trí: {max_index}")
print(f"Phần tử nhỏ nhất trong danh sách: {min_value}, Vị trí: {min_index}")
print(f"Danh sách sau khi sắp xếp: {sorted_list}")
