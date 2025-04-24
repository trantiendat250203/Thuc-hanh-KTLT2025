from tkinter import *
#tao cua so do hoa
window = Tk()
window.title("Welcome to LikeGeeks app") # tieu de cua so
window.geometry('350x200') # kich thuc cua so
# them 1 label de hien thi van ban
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)  # # dat label tai vi tri cot 0 hang 0
# phuong thuc xu ly khi nut clickme dc nhan
def clicked():
    lbl.configure(text="Button was clicked !!")
# them 1 nut button vao cua so
btn = Button(window, text="Click Me", command=clicked, bg="green", fg="white")  
btn.grid(column=1, row=0)  # dat button tai vi tri cot 1 hang 0
# vong lap chinh de duy tri cua so hoat dong
window.mainloop()
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")