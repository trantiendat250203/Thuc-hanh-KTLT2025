def read_first_n_lines(file_path, n):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for i in range(n):
                line = file.readline()  
                if not line:            
                    break
                print(line.strip())      
    except FileNotFoundError:
        print("File không tồn tại. Vui lòng kiểm tra lại đường dẫn.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
read_first_n_lines('hieu.txt', 1)
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")