print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")
 
from tkinter import* # Nhập toàn bộ thư viện tkinter để dùng các hàm, widget như Menu, Tk, mainloop.
def NewFile(): #Khi người dùng chọn File > New, in ra "New File!".
    print("New File!")
def OpenFile():#Khi chọn File > Open, in ra "Open File()".
    print("Open File()")
def Exit():#Khi chọn File > Exit, in "Exit()" rồi thoát ứng dụng.
    print("Exit()")
    root.quit()
def InsText():#Khi chọn Insert > Text in thông báo tương ứng
    print("InsTex()")
def InsPic():#chọn Insert > Picture,in thông báo tương ứng
    print("InsPic()")
def About(): #Khi chọn Help > About..., in mô tả ngắn về ứng dụng.
    print("This is a simple example of a menu") 
root = Tk() # Tạo cửa sổ chính.
menu = Menu(root) #
root.config(menu=menu) 
filemenu = Menu(menu) 
menu.add_cascade(label="File", menu=filemenu) 
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator() 
filemenu.add_command(label="Exit", command=root.quit)

insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

helpmenu = Menu(menu) 
menu.add_cascade(label="Help", menu=helpmenu) 
helpmenu.add_command(label="About...", command=About) 
mainloop() 
