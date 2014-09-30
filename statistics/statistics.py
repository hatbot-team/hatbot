import os
import pickle

PICKLE_PROTOCOL = 3
DEFAULT_STATISTICS_PATH = os.path.dirname(os.path.abspath(__file__)) + "/statistics"
DEFAULT_BLACKLIST_PATH = os.path.dirname(os.path.abspath(__file__)) + "/blacklist"

class Statistics:
    def __init__(self,
                 stat_path=DEFAULT_STATISTICS_PATH):
        self._path = stat_path
        self._stat = dict()

        if stat_path is not None:
            try:
                self.load(stat_path)
            except FileNotFoundError:
                pass

    def load(self, path):
        stat_file = open(self._path, "rb")
        self._stat.clear()
        while True:
            try:
                explanation = pickle.load(stat_file)
            except EOFError:
                stat_file.close()
                return
            cnt_all = pickle.load(stat_file)
            cnt_win = pickle.load(stat_file)
            self._stat[explanation] = (cnt_all, cnt_win)

    def update(self, explanation, result):
        if result not in {'SUCCESS', 'FAIL'}:
            raise AttributeError('explanation result should be either "SUCCESS" or "FAIL"')

        cnt_all, cnt_win = self._stat.get(explanation, (0, 0))
        cnt_all += 1
        if result == 'SUCCESS':
            cnt_win += 1
        self._stat[explanation] = (cnt_all, cnt_win)

    def save(self, path=None):
        if path is None:
            path = self._path
        if path is None:
            raise AttributeError("Don't know where to save statistics")

        stat_file = open(path, "wb")
        for expl, (cnt_all, cnt_win) in self._stat.items():
            pickle.dump(expl, stat_file, PICKLE_PROTOCOL)
            pickle.dump(cnt_all, stat_file, PICKLE_PROTOCOL)
            pickle.dump(cnt_win, stat_file, PICKLE_PROTOCOL)
        stat_file.close()

    def entries(self):
        return self._stat.items()

class BlackList:
    def __init__(self, path=DEFAULT_BLACKLIST_PATH):
        self._path = path
        self._blacklist = dict()

        if path is not None:
            try:
                self.load(path)
            except FileNotFoundError:
                pass

    def load(self, path):
        blacklist_file = open(path, 'rb')
        self._blacklist.clear()
        while True:
            try:
                explanation = pickle.load(blacklist_file)
            except EOFError:
                blacklist_file.close()
                return
            cnt = pickle.load(blacklist_file)
            self._blacklist[explanation] = cnt

    def blame(self, explanation):
        self._blacklist.setdefault(explanation, 0)
        self._blacklist[explanation] += 1

    def save(self, path=None):
        if path is None:
            path = self._path
        if path is None:
            raise AttributeError("Don't know where to save black list")

        black_file = open(path, "wb")
        for expl, cnt in self._blacklist.items():
            pickle.dump(expl, black_file, PICKLE_PROTOCOL)
            pickle.dump(cnt, black_file, PICKLE_PROTOCOL)
        black_file.close()

    def entries(self):
        return self._blacklist.items()
