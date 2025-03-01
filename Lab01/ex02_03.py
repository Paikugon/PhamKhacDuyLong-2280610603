#Nhập một số nguyên và kiểm tra có chẵn hay không
#check if a number is even or not
def is_even(n):
    return n % 2 == 0

try:
    number = int(input("Nhập số cần kiểm tra: "))
    if is_even(number):
        print("Số", number, "là số chẵn")
    else:
        print("Số", number, "là số lẻ")
except ValueError:
    print("Bạn đã nhập không phải là số nguyên")

