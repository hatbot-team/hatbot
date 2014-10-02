import explanator
from statistics.statistics import Statistics, BlackList

__author__ = 'pershik'


def interact():
    stat = Statistics()
    black = BlackList()

    while True:
        print("Объяснение: ")
        word = explanator.get_random_word()
        explanation = explanator.explain(word)
        print(explanation)

        input("Нажмите enter, чтобы узнать ответ")
        print("Ответ: " + word)

        result = input("Угадали? Если объяснение некорректно, введите i. (y/n/i) ")
        while result != "y" and result != "n" and result != "i":
            result = input("Некорректный ввод. Введите y/n/i ")
        if result == 'i':
            black.blame(explanation)
        else:
            stat.update(explanation, 'SUCCESS' if result == 'y' else 'FAIL')

        result = input("Продолжить? (y/n) ")
        while result != "y" and result != "n":
            result = input("Некорректный ввод. Введите y/n ")
        if result == "n":
            print("Спасибо!")
            break
    stat.save()
    black.save()

if __name__ == '__main__':
    interact()
