from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog
# ham xu ly ki chon "New" trong menu "File"
def NewFile():
    print("New File!")

# ham xu ly khi chon "Open" trong menu "File"
def OpenFile():
    filename = filedialog.askopenfilename(title="Open a File")
    if filename:  # neu nguoi dung chon mot tep tin
        print(f"Open File: {filename}")
    else:
        print("No file selected")
# ham xu ly khi chon "Exit" trong menu "File"
def ExitApp():
    print("Exit Application")
    root.quit()  # dong cua so
# ham xu ly khi chon "Insert Text" trong menu "Insert"
def InsText():
    text = simpledialog.askstring("Input", "Enter your text:")
    if text:  # neu nguoi dung nhap van ban
        print(f"Inserted Text: {text}")
        label.config(text=text)  # cap nhat van ban hien thi trong cua so
    else:
        print("No text inserted")
# ham xu ly khi chon "Insert Picture" trong menu "Insert"
def InsPic():
    filename = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif")])
    if filename:  # neu nguoi dung chon hinh anh
        print(f"Inserted Picture: {filename}")
        img = Image.open(filename)
        img.thumbnail((200, 200))  # kich thuoc hinh anh
        img = Imagetk.PhotoImage(img)
        label.config(image=img, text="")  # hien thi anh trong cua so
        label.image = img  
    else:
        print("No image selected")
# Hàm xử lý khi người dùng chọn "About..." trong menu "Help"
def About():
    print("This is a simple example of a menu")
# tao cua so chinh
root = Tk()
root.title("Simple Menu Example")
# tao mot doi tuong menu
menu = Menu(root)
root.config(menu=menu)  # gan menu cho cua so chinh
# Tao menu con "File" và them cac muc vao menu
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=ExitApp)
# Tao menu con "Insert" giua "File" va "Help"
insertmenu = Menu(menu)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Insert Text", command=InsText)
insertmenu.add_command(label="Insert Picture", command=InsPic)
# Tao menu con "Help" va them cac muc vao menu nay
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)
# them mot label de hien thi van ban hoac anh chen vao
label = Label(root, text="Welcome!", width=40, height=10)
label.pack(padx=10, pady=10)
# chay vong lap chinh de giao dien hien thi 
root.mainloop()
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")
