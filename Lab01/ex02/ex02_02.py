#Nhập bán kính hình tròn và tính diện tích hình tròn
#check if ban kinh is a number
while True:
    try:
        r = float(input("Nhập bán kính hình tròn: "))
        break
    except ValueError:
        print("Bán kính phải là số")
#tinh dien tich hinh tron
S = 3.14 * r * r
print("Diện tích hình tròn có bán kính", r, "là", S)