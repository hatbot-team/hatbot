from . import langenums as langenums


class GrammarInfo:
    def __init__(self, grammar):
        self.__repr = grammar
        a = []
        for i in [x.split(',') for x in grammar.split('=')]:
            a.extend(i)
        for gr in a:
            if gr not in {'', 'praet', 'reserved'}:
                parsed = False
                for name, iterclass in langenums.__dict__.items():
                    if name[0] != '_':
                        try:
                            q = iterclass(gr)
                            if name == 'Other':
                                if name not in self.__dict__:
                                    self.__dict__[name] = set()
                                self.__dict__[name].add(q)
                            else:
                                self.__dict__[name] = q
                            parsed = True
                            break
                        except ValueError:
                            pass
                if not parsed:
                    raise Exception(gr + ' don\'t parsed')

    def __repr__(self):
        return self.__repr



class AnalysisInfo:
    def __init__(self, analysis):
        self.lex = None
        if 'lex' in analysis.keys():
            self.lex = analysis['lex']
        self.frequency = None
        if 'wt' in analysis.keys():
            self.frequency = float(analysis['wt'])
        self.quality = 1
        if 'qual' in analysis.keys():
            if analysis['qual'] == 'bastard':
                self.quality = 0
        self.grammar = None
        if 'gr' in analysis.keys():
            self.grammar = GrammarInfo(analysis['gr'])
        for x in analysis.keys():
            if x not in {'lex', 'wt', 'qual', 'gr'}:
                raise ValueError('Undetected analysis term')

    def __repr__(self):
        return 'lex:' + self.lex + ',gr:' + self.grammar.__repr__()


class WordInfo:
    def __init__(self, json):
        self.text = json['text']
        if 'analysis' in json.keys():
            self.analysis = [AnalysisInfo(i) for i in json['analysis']]
        else:
            self.analysis = None
    def __str__(self):
        return '<text:' + self.text + ',' + self.analysis.__repr__() + '>'

    def __repr__(self):
        return str(self)
