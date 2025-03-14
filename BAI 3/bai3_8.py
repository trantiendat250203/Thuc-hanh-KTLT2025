import math
pos = [0, 0]
while True:
    s = input("Nhập lệnh di chuyển (hoặc nhấn Enter để dừng): ")
    if not s:
        break
    movement = s.split(" ")  
    direction = movement[0]  
    steps = int(movement[1])  
    
    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else:
        pass  

distance = math.sqrt(pos[0]**2 + pos[1]**2)
print(int(round(distance)))
print ("sinh vien: Tran Van Tien Dat")
print ("Mssv: 235752020710004")