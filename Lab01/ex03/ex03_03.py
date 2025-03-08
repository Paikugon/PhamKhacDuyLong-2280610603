def ListToTuple(lst):
    return tuple(lst)

strInput = input("Nhập một dãy số, cách nhau bởi dấu phẩy: ")
inputList = list(map(int, strInput.split(",")))
newTuple = ListToTuple(inputList)
print("List: ", inputList)
print("Tuple: ", newTuple)
