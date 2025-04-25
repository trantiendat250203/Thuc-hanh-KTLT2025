def read_and_reverse_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines() 
            content.reverse()             
            for line in content:
                print(line.strip())     
    except FileNotFoundError:
        print("File không tồn tại. Vui lòng kiểm tra lại đường dẫn.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
read_and_reverse_file('dat.txt')
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")
