print("Đậu Văn Quốc Bảo")
print("MSSV:235752020710014")

def sequential_search(dlist, item):
    """
    Hàm tìm kiếm tuyến tính trong danh sách dlist.
    Trả về một tuple (True, index) nếu tìm thấy phần tử.
    Nếu không tìm thấy, trả về (False, -1).
    """
    for i in range(len(dlist)):
        if dlist[i] == item:
            return (True, i)
    return (False, -1)

if __name__ == "__main__":

    # Nhập dãy số từ bàn phím và chuyển thành danh sách các số nguyên
    dlist = list(map(int, input("Nhập dãy số (các số cách nhau bằng dấu cách): ").split()))
    # Nhập phần tử cần tìm
    item = int(input("Nhập phần tử cần tìm: "))
    
    # Gọi hàm tìm kiếm
    result = sequential_search(dlist, item)

    # In kết quả
    if result[0]:
        print(f"Phần tử {item} được tìm thấy tại chỉ mục {result[1]}.")
    else:
        print(f"Phần tử {item} không có trong danh sách.")
