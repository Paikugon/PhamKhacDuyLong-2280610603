#reverse an array
def reverse_array(arr):
    return arr[::-1]

strInput = input("Nhập một dãy số, cách nhau bởi dấu phẩy: ")
inputList = list(map(int, strInput.split(",")))
print("Tổng các số chẵn trong dãy số là:", reverse_array(inputList))