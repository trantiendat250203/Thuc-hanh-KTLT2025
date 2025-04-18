def analyze_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.readlines() 
        
            num_lines = len(content)     
            num_chars = sum(len(line) for line in content)  
            num_words = sum(len(line.split()) for line in content) 
            
            print(f"Số dòng: {num_lines}")
            print(f"Số ký tự: {num_chars}")
            print(f"Số từ: {num_words}")
            
    except FileNotFoundError:
        print("File không tồn tại. Vui lòng kiểm tra lại đường dẫn.")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")
analyze_file('hieu.txt')
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")