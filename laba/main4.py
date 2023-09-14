word = input("Введите со скобками: ")
cnt1 = word.count(")")
cnt2 = word.count("(")
if cnt1 == 0 and cnt2 == 0:
    print("Нет скобок")
else:
    for i in word:
        if cnt1 > cnt2:
            print("Закрывающихся скобок больше")
            break
        elif cnt1 < cnt2:
            print("Открывающихся скобок больше")
            break
        elif cnt1 == cnt2:
            print(word)
            break
