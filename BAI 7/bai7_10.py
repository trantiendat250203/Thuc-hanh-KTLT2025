def find_longest_words(text):
    words = text.split()
    max_length = len(max(words, key=len))
    longest_words = [word for word in words if len(word) == max_length]
    return longest_words
text = """tran van tien dat sinh vien nganh dien tu vien thong vien ky thuat cong nghe truong dai hoc vinh"""
print(find_longest_words(text))
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")
