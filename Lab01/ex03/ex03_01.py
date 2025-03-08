def sumEven(list):
    sum = 0
    for i in list:
        if i % 2 == 0:
            sum += i
    return sum

strinputList = input("Nhập một dãy số, cách nhau bởi dấu phẩy: ")
inputList = list(map(int, strinputList.split(",")))
print("Tổng các số chẵn trong dãy số là:", sumEven(inputList))