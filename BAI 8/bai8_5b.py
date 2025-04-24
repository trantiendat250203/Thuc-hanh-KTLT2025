import tkinter as tk
root = tk.Tk()
root.title("Programming Language Selection")
v = tk.IntVar()
v.set(1)
languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]
def ShowChoice():
    print(f"Bạn đã chọn: {languages[v.get() - 1][0]}")
tk.Label(root, text="Choose your favourite programming language:", justify=tk.LEFT, padx=20).pack()
for text, value in languages:
    tk.Radiobutton(root, 
                   text=text, 
                   indicatoron=0, 
                   width=20,       
                   padx=20,       
                   variable=v,    
                   command=ShowChoice,
                   value=value     
                  ).pack(anchor=tk.W)
root.mainloop()
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")