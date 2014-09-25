import os
import pickle

__author__ = 'pershik'

stat_name = os.path.dirname(os.path.abspath(__file__)) + "/statistic"
bad_name = os.path.dirname(os.path.abspath(__file__)) + "/bad_expl"

print("Statistic:")
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

print("\n\nBad explanations:")
bad_file = open(bad_name, "rb")
while True:
    try:
        expl = pickle.load(bad_file)
    except:
        bad_file.close()
        break
    print(expl)