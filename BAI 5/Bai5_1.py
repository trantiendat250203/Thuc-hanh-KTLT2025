## My script using the math module ## 
print("sinh vien: Tran Van Tien Dat")
print("MSSV:235752020710004")
import mymath  # Note no .py 
values = [2,4,6,8,10] 
print('Squares:') 
for v in values: 
    print(mymath.square(v)) 
print ('Cubes:')
for v in values: 
    print(mymath.cube(v)) 
print('Average: ' + str(mymath.average(values)))
