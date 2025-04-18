class RomanToInteger:
    def __init__(self):
   
        self.roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

    def convert(self, roman):
        total = 0
        prev_value = 0
        
        for char in reversed(roman):
            value = self.roman_numerals.get(char, 0)
            if value < prev_value:
                total -= value  
            else:
                total += value  
            prev_value = value
        
        return total

converter = RomanToInteger()
roman_number = "MCMXCIV"  
integer_value = converter.convert(roman_number)

print(f"Số La Mã '{roman_number}' chuyển đổi thành số nguyên là: {integer_value}")
print("sinh vien: Tran Van Tien Dat")
print("Mssv: 235752020710004")