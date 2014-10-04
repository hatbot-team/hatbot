import os
from utils import json_hooks as json


class Statistics:
    DEFAULT_PATH = os.path.dirname(os.path.abspath(__file__)) + "/statistics.json"

    def __init__(self, stat_path=DEFAULT_PATH):
        self._path = stat_path
        self._stat = dict()

        if stat_path is not None:
            try:
                self.load(stat_path)
            except FileNotFoundError:
                pass

    def load(self, path):
        with open(self._path, "r") as stat_file:
            self._stat = json.load(stat_file)

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

        with open(path, "w") as stat_file:
            json.dump(self._stat, stat_file, indent='\t')

    def entries(self):
        return self._stat.items()


class BlackList:
    DEFAULT_PATH = os.path.dirname(os.path.abspath(__file__)) + "/blacklist.json"

    def __init__(self, path=DEFAULT_PATH):
        self._path = path
        self._blacklist = dict()

        if path is not None:
            try:
                self.load(path)
            except FileNotFoundError:
                pass

    def load(self, path):
        with open(path, 'r') as black_file:
            self._blacklist = json.load(black_file)

    def blame(self, explanation):
        self._blacklist.setdefault(explanation, 0)
        self._blacklist[explanation] += 1

    def save(self, path=None):
        if path is None:
            path = self._path
        if path is None:
            raise AttributeError("Don't know where to save black list")

        with open(path, "w") as black_file:
            json.dump(self._blacklist, black_file, indent='\t')

    def entries(self):
        return self._blacklist.items()
