import tkinter as tk
# cua so chinh
root = tk.Tk()
root.title("Programming Language Selection")
# Khai bao bien IntVar de luu gia tri cua radio button da chon
v = tk.IntVar()
v.set(1)  # khoi tao lua chon mac dinh
# danh sach cac lua chon ngon ngu lap trinh
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]
# ham xu ly khi chon 1 radio button
def ShowChoice():
    # In ra gia tri lua chon da chon trong bien v
    print(f"Bạn đã chọn: {languages[v.get() - 1][0]}")
# Them Label gioi thieu cho nguoi dung
tk.Label(root, text="Choose your favourite programming language:", justify=tk.LEFT, padx=20).pack()
# tao cac radio button cho cac lua chon
for text, value in languages:
    # Tao radio button cho moi ngon ngu
    tk.Radiobutton(root, text=text, padx=20, variable=v, command=ShowChoice, value=value).pack(anchor=tk.W)
# chay vong lap chinh de giao dien hien thi
root.mainloop()
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")