input_str = input("Nhập x, y: ")
x, y = input_str.split(',')
x = int(x)
y = int(y)

a = [[0 for i in range(y)] for j in range(x)]
for i in range(x):
    for j in range(y):
        a[i][j] = i*j
print(a)