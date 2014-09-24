import os
import pickle

__author__ = 'pershik'

stat_name = os.path.dirname(os.path.abspath(__file__)) + "/statistic"

stat_file = open(stat_name, "rb")
while True:
    try:
        expl = pickle.load(stat_file)
    except:
        stat_file.close()
        break
    cnt_all = pickle.load(stat_file)
    cnt_win = pickle.load(stat_file)
    print(expl, cnt_all, cnt_win)