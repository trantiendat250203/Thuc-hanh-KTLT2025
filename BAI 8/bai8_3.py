import turtle
colors = ["red", "blue", "green"]
painter = turtle.Turtle()
painter.pensize(3)
for i in range(12):
    color = colors[i % len(colors)]  # chon mau theo thu tu
    painter.pencolor(color)           # dat mau cho but ve
    painter.circle(100)               # ban kinh
    painter.right(30)                 # quay 30 do sang phai
    painter.left(60)                  # quay 60 do sang trai
    painter.setposition(0, 0)         # dat lai vi tri (0,0)
turtle.done()
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")