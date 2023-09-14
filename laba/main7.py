from random import randint

pc_num = randint(0, 100)
while True:
    num = int(input("Введите число: "))
    if num == pc_num:
        print("Поздравляю! Вы выиграли 1 000 000$")
        break
    elif num > pc_num:
        print("Меньше")
    elif num < pc_num:
        print("Больше")
