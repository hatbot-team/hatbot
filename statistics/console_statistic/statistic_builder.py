import pickle
import random
import os

import explanator

__author__ = 'pershik'

PICKLE_PROTOCOL = 3

stat_name = os.path.dirname(os.path.abspath(__file__)) + "/statistic"
bad_name = os.path.dirname(os.path.abspath(__file__)) + "/bad_expl"
words = list(explanator.get_explainable_words())
stat = dict()
bad_expl = set()


def init_stat():
    try:
        stat_file = open(stat_name, "rb")
        while True:
            try:
                expl = pickle.load(stat_file)
            except:
                stat_file.close()
                return
            cnt_all = pickle.load(stat_file)
            cnt_win = pickle.load(stat_file)
            stat[expl] = (cnt_all, cnt_win)
    except:
        return


def init_bad():
    try:
        bad_file = open(bad_name, "rb")
        while True:
            try:
                expl = pickle.load(bad_file)
            except:
                bad_file.close()
                return
            bad_expl.add(expl)
    except:
        return


def init():
    init_stat()
    init_bad()


def update_stat(expl, res):
    if result == "i":
        bad_expl.add(expl)
    val = (0, 0)
    if expl in stat:
        val = stat[expl]
    win = 0
    if res == "y":
        win = 1
    stat[expl] = (val[0] + 1, val[1] + win)


def save_stat():
    stat_file = open(stat_name, "wb")
    for expl in stat.keys():
        pickle.dump(expl, stat_file, PICKLE_PROTOCOL)
        pickle.dump(stat[expl][0], stat_file, PICKLE_PROTOCOL)
        pickle.dump(stat[expl][1], stat_file, PICKLE_PROTOCOL)
    stat_file.close()


def save_bad():
    bad_file = open(bad_name, "wb")
    for expl in bad_expl:
        pickle.dump(expl, bad_file, PICKLE_PROTOCOL)
    bad_file.close()


def save():
    save_stat()
    save_bad()


init()
while True:
    print("Объяснение: ")
    word = random.choice(words)
    explanation = explanator.explain(word)
    print(explanation)

    print("Нажмите enter, чтобы узнать ответ", end="")
    input()
    print("Ответ: " + word)

    print("Угадали? (y/n) \nЕсли объяснение некорректно, введите i")
    result = input()
    while result != "y" and result != "n" and result != "i":
        print("Некорректный ввод. Введите y/n/i")
        result = input()
    update_stat(explanation, result)

    print("Продолжить? (y/n)")
    result = input()
    while result != "y" and result != "n":
        print("Некорректный ввод. Введите y/n")
        result = input()
    if result == "n":
        print("Спасибо!")
        break
save()