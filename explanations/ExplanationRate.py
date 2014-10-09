__author__ = 'Алексей'


class ExplanationRate:

    def __init__(self, priory_rate=0, source_rate=0, statistics_rate=0):
        """
        class represents comparable rate of current explanation.
        global rate consists of 3 rates:
        :param priory_rate: value based on priory estimates of explanation. Number from [0, 100]
        :param source_rate: value based on rate of current explanation source. Number from [0, 100]
        :param statistics_rate: value based on statistics. Number from [0, 100]
        """
        self.priority_rate = priory_rate
        self.source_rate = source_rate
        self.statistics_rate = statistics_rate

    def key(self):
        return self.priority_rate + self.source_rate + self.statistics_rate

    def __lt__(self, other):
        return self.key() < other.key()
