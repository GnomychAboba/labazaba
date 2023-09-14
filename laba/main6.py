word = input("Введите: ")
equal = []
for i in word:
    if i.isdigit():
        equal.append(i)

inp = int(input("Введите положение числа: "))
print(equal[inp-1])
