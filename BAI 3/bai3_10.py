import math

def Tinh(R):
    if R < 0:
        return "Bán kính không hợp lệ. Vui lòng nhập một giá trị dương."
   
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R**2
    
    return chu_vi, dien_tich

try:
    R = float(input("Nhập bán kính R: "))
    result = Tinh(R)
    
    if isinstance(result, str):
        print(result)  
    else:
        chu_vi, dien_tich = result
        print(f"Chu vi hình tròn: {chu_vi:.2f}")
        print(f"Diện tích hình tròn: {dien_tich:.2f}")
except ValueError:
    print("Giá trị nhập vào không hợp lệ! Vui lòng nhập một số.")
print ("sinh vien: Tran Van Tien Dat")
print ("Mssv: 235752020710004")