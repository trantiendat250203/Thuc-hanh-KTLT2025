import datetime as dt

# Định dạng thời gian
format = '%Y-%m-%dT%H:%M:%S'

# Phân tích chuỗi thời gian
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)

# In ra các thành phần của thời gian
print('Day: ' + str(t1.day))
print('Month: ' + str(t1.month))
print('Minute: ' + str(t1.minute))
print('Second: ' + str(t1.second))

# Định nghĩa ngày và giờ hiện tại
t2 = dt.datetime.now()

# Tính hiệu giữa hai thời điểm
diff = t2 - t1
print('How many days difference? ' + str(diff.days))
print ("sinh vien: Tran Van Tien Dat")
print ("Mssv: 235752020710004")