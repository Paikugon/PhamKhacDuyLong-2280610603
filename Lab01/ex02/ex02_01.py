#Nhap ten va tuoi nguoi dung
ten = input("Nhập tên của bạn: ")

while True:
    try:
        tuoi = int(input("Nhập tuổi của bạn: "))
        break
    except ValueError:
        print("Tuổi phải là số nguyên")

print("Chào mừng", ten + "!Tuổi của bạn là", tuoi, "tuổi")
