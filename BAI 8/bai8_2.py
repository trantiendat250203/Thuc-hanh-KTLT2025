import turtle
import random
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]
painter = turtle.Turtle()
painter.pensize(3)
for i in range(10):
    color = random.choice(colors)  # chon mau tu ds
    painter.pencolor(color)        # dat mau cho but ve
    painter.circle(100)            # ban kinh 100
    painter.right(30)              # quy sang phai 30 do 
    painter.left(60)               # quay san trai 60 do
    painter.setposition(0, 0)      # dat lia ve vi tri (0,0)
turtle.done()
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")