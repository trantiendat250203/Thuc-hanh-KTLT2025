import tkinter as tk
# ham hien thi thong tin khui nguoi dung nha "Click Me"
def show_choice():
    selected_value = radio_var.get()  
    label_result.config(text=f"Lựa chọn của bạn là: {selected_value}")
root = tk.Tk()
root.title("welcome")  # tieu de
root.geometry("400x200")  # kich thuoc
# bien luu tru gia tri cua Radio Button
radio_var = tk.StringVar(value="1")  # mac dinh chon "1"
# frame de chua cac radio buttons va nut "Click Me" theo chieu ngang
frame_radio = tk.Frame(root)
frame_radio.pack(pady=10)
radio_button1 = tk.Radiobutton(frame_radio, text="first", variable=radio_var, value="1")
radio_button1.pack(side="left", padx=10)
radio_button2 = tk.Radiobutton(frame_radio, text="second", variable=radio_var, value="2")
radio_button2.pack(side="left", padx=10)
radio_button3 = tk.Radiobutton(frame_radio, text="third", variable=radio_var, value="3")
radio_button3.pack(side="left", padx=10)
button_click = tk.Button(frame_radio, text="Click Me", command=show_choice)
button_click.pack(side="left", padx=10)
# Label de hien thi ket qua luu chon
label_result = tk.Label(root, text="", font=('Helvetica', 12))
label_result.pack(pady=10)
root.mainloop()
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")