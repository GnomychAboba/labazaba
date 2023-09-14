arr = []
rev = ""
while True:
    num = input("Введите число: ")
    if not num.isdigit():
        break
    else:
        arr.append(num)
        rev = sorted(arr, reverse=True)

for i in rev:
    print(i, end="")

