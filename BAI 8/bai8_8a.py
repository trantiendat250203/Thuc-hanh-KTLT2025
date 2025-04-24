import tkinter as tk
# Hàm để hiển thị thông tin sau khi người dùng nhập
def show_info():
    name = entry_name.get()
    dob = entry_dob.get()
    mssv = entry_mssv.get()
    major = entry_major.get()
    # Hiển thị thông tin
    label_result.config(text=f"Họ tên: {name}\nNgày sinh: {dob}\nMSSV: {mssv}\nNgành học: {major}")
root = tk.Tk()
root.title("Thông Tin Cá Nhân")  # Tiêu đề 
root.geometry("400x300")  # Kích thước 
# label hướng dẫn
label_instructions = tk.Label(root, text="Nhập thông tin cá nhân", font=('Helvetica', 14))
label_instructions.pack(pady=10)
# Label và Entry cho Họ tên
label_name = tk.Label(root, text="Họ và Tên:")
label_name.pack()
entry_name = tk.Entry(root, width=30)
entry_name.pack(pady=5)
# Label và Entry cho Ngày tháng năm sinh
label_dob = tk.Label(root, text="Ngày sinh (dd/mm/yyyy):")
label_dob.pack()
entry_dob = tk.Entry(root, width=30)
entry_dob.pack(pady=5)
# Label và Entry cho MSSV
label_mssv = tk.Label(root, text="MSSV:")
label_mssv.pack()
entry_mssv = tk.Entry(root, width=30)
entry_mssv.pack(pady=5)
# Label và Entry cho Ngành học
label_major = tk.Label(root, text="Ngành học:")
label_major.pack()
entry_major = tk.Entry(root, width=30)
entry_major.pack(pady=5)
# Nút hiển thị thông tin
button_show = tk.Button(root, text="Hiển thị thông tin", command=show_info)
button_show.pack(pady=10)
# Label hiển thị kết quả thông tin sau khi người dùng nhập
label_result = tk.Label(root, text="", font=('Helvetica', 12))
label_result.pack(pady=10)
root.mainloop()
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")