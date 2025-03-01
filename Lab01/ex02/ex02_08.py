def isDivisible(num):
    new_num = int(num, 2)
    if new_num % 5 == 0:
        return True
    else:
        return False

input_str = input("Nhập các số nhị phân: ")
list = input_str.split(',')
flag = False # flag to check if there is any number divisible by 5
for i in list:
    if isDivisible(i):
        print(i)
        flag = True
if not flag:
    print("Không có số nào chia hết cho 5")
