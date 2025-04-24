import tkinter
import random
# List mau sac
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 
           'Yellow', 'Orange', 'White', 'Purple', 'Brown'] 
score = 0  # diem so ban dau
timeleft = 120  # thoi gian choi
def startGame(event):
    global score, timeleft
    if timeleft == 120:
        countdown()
        #ham chon mau sac tiep
        nextColour()
# ham chon và hien thi mau sac tiep theo
def nextColour():
    global score, timeleft
    if timeleft > 0:
        e.focus_set()
        # tra loi dung cong 2, sai tru 1
        if e.get().lower() == colours[1].lower():
            score += 2
        else:
            score -= 1
        e.delete(0, tkinter.END)  # xoa noi dung trong o nhap
        random.shuffle(colours)  # tron ds mau sac
        # cap nhat mau sac va van ban
        label.config(fg=str(colours[1]), text=str(colours[0]))
        # diem so
        scoreLabel.config(text="Score: " + str(score))
# ham dem nguoc thoi gian
def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1  # giam thoi gian con lai
        timeLabel.config(text="Time left: " + str(timeleft))  # cap nhat label thoi gian
        timeLabel.after(1000, countdown)  # goi lai ham sau 1s
# tao cua so GUI
root = tkinter.Tk()
root.title("COLORGAME")  # tieu de
root.geometry("375x250")  # kich thuoc
# them label huong dan
instructions = tkinter.Label(root, text="Type in the colour of the words, and not the word text!",
                             font=('Helvetica', 12))
instructions.pack()
# them label hien thi diem so
scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()
# them label hien thi thoi gian con lai
timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft), font=('Helvetica', 12))
timeLabel.pack()
# them label hien thi mau sac
label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()
# them o de nhap cau tra loi
e = tkinter.Entry(root)
e.pack()
e.focus_set()
root.bind('<Return>', startGame)
root.mainloop()
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")