#check if a number is prime or not
def is_prime(n):
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
    if (n % 2 == 0 or n % 3 == 0) :
        return False
    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6
    return True

try :
    number = int(input("Nhập số cần kiểm tra: "))
    if is_prime(number):
        print("Số", number, "là số nguyên tố")
    else:
        print("Số", number, "không phải là số nguyên tố")
except ValueError:
    print("Bạn đã nhập không phải là số nguyên")