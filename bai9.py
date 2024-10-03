def number_to_words(number):
    # Định nghĩa các từ số từ 1 đến 19
    ones = ["", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín",
            "mười", "mười một", "mười hai", "mười ba", "mười bốn", "mười lăm",
            "mười sáu", "mười bảy", "mười tám", "mười chín"]
    
    # Định nghĩa các từ hàng trăm
    hundreds = ["", "một trăm", "hai trăm", "ba trăm", "bốn trăm", "năm trăm",
                "sáu trăm", "bảy trăm", "tám trăm", "chín trăm"]
    
    if number == 0:
        return "Không"
    elif number < 20:
        return ones[number]
    elif number < 100:
        tens_digit = number // 10
        ones_digit = number % 10
        return ones[tens_digit] + " mươi " + ones[ones_digit]
    else:
        hundreds_digit = number // 100
        remainder = number % 100
        return hundreds[hundreds_digit] + " " + number_to_words(remainder)
def main():
    number = int(input("Nhập một số từ 1 đến 999: "))
    if 1 <= number <= 999:
        words = number_to_words(number)
        print(f"{number} được viết thành chữ là: {words}")
    else:
        print("Số bạn nhập không nằm trong khoảng từ 1 đến 999.")

if __name__ == "__main__":
    main()
