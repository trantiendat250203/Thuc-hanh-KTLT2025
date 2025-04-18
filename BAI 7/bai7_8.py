def write_list_to_file(fname, data_list):
    with open(fname, 'w') as file:
        for item in data_list:
            file.write(f"{item}\n") 
my_list = ["Python", "Java", "C++", "JavaScript", "Ruby"]
file_name = 'output.txt'
write_list_to_file(file_name, my_list)
print(f"Nội dung của danh sách đã được ghi vào tệp '{file_name}'.")
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")