num = input("Введите пятизначное число: ")

if len(num) != 5 or not num.isdigit():
    print("Не пятизначное число")
else:
    for i in num:
        print(i)
