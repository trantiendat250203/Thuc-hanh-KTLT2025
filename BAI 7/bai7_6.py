import os
def file_read_from_tail(fname, lines):
    bufsize = 8192
    fsize = os.stat(fname).st_size
    iter = 0
    data = []
    with open(fname) as f:
        if bufsize > fsize:
            bufsize = fsize           
        while True:
            iter += 1
            f.seek(fsize - bufsize * iter)
            data.extend(f.readlines())
            if len(data) >= lines or f.tell() == 0:
                print(''.join(data[-lines:]))
                break
file_read_from_tail('dat.txt', 2)
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")
