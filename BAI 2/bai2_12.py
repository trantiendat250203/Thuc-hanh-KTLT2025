import re
valid_passwords = []
passwords = input("Nhap mat khau, cach nhau boi dau phay: ").split(',')
for p in passwords:
    p = p.strip()
    if len(p) < 6 or len(p) > 12:
        continue
    if not re.search("[a-z]", p):
        continue
    if not re.search("[0-9]", p):
        continue
    if not re.search("[A-Z]", p):
        continue
    if not re.search("[$#@]", p):
        continue
    if re.search("\s", p):
        continue
    valid_passwords.append(p)
print(",".join(valid_passwords))
print ("sinh vien: Tran Van Tien Dat")
print ("Mssv: 235752020710004")