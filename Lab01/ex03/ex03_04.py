def FirstAndLastElement(tuple):
    return tuple[0], tuple[-1]

inputTuple = eval(input("Nhập một tuple: "))
first, last = FirstAndLastElement(inputTuple)
print("Phần tử đầu tiên: ", first)
print("Phần tử cuối cùng: ", last)
