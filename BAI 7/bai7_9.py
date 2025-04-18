def copy_file_content(source_file, destination_file):
    with open(source_file, 'r') as src:
        with open(destination_file, 'w') as dest:
            content = src.read()  
            dest.write(content) 
source_file_name = 'hieu.txt' 
destination_file_name = 'destination.txt'  
copy_file_content(source_file_name, destination_file_name)
print(f"Nội dung của tệp '{source_file_name}' đã được sao chép sang tệp '{destination_file_name}'.")
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")