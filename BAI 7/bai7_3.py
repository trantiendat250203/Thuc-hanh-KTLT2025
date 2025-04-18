def read_entire_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()  
            print(content)     
    except FileNotFoundError:
        print("File không tồn tại. Vui lòng kiểm tra lại đường dẫn.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
read_entire_file('hieu.txt')
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")