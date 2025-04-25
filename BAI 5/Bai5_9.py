# main.py
print("Đậu Văn Quốc Bảo")
print("MSSV:235752020710014")
import binary_search

if __name__ == "__main__":

    # Nhập dãy số từ bàn phím và chuyển thành danh sách các số nguyên
    n = int(input("Nhập số lượng phần tử trong danh sách: "))
    dlist = list(map(int, input(f"Nhập {n} phần tử (các số cách nhau bằng dấu cách): ").split()))

    # Sắp xếp danh sách để áp dụng thuật toán tìm kiếm nhị phân
    dlist.sort()

    # Nhập phần tử cần tìm
    value = int(input("Nhập phần tử cần tìm: "))

    # Gọi hàm tìm kiếm nhị phân
    result = binary_search.binary_search(dlist, value)

    # In kết quả
    if result:
        print(f"Phần tử {value} được tìm thấy trong danh sách.")
    else:
        print(f"Phần tử {value} không có trong danh sách.")
