# -*- coding: utf-8 -*-

from enum import Enum as _Enum


class PartsOfSpeech(_Enum):
    '''
    Части речи:
        Adjective - прилагательное
        Adverb  - наречие
        PronominalAdverb - местоименное наречие
        NumeralAdjective - числительное-прилагательное
        PronounAdjective - местоимение-прилагательное
        PartOfCompoundWord - часть сложного слова
        Conjunction - союз
        Interjection - междометие
        Numeral - числительное
        Particle - частица
        Preposition - предлог
        Noun - существительное
        NounPronoun - местоимение-существительное
        Verb - глагол
    '''
    Adjective = 'A'
    Adverb = 'ADV'
    PronominalAdverb = 'ADVPRO'
    NumeralAdjective = 'ANUM'
    PronounAdjective = 'APRO'
    PartOfCompoundWord = 'COM'
    Conjunction = 'CONJ'
    Interjection = 'INTJ'
    Numeral = 'NUM'
    Particle = 'PART'
    Preposition = 'PR'
    Noun = 'S'
    NounPronoun = 'SPRO'
    Verb = 'V'



class Time(_Enum):
    '''
    Время глагола:
        Present - настоящее
        Inpresent - непрошедшее
        Past - прошедшее
    '''
    Present = 'praes'
    Inpresent = 'inpraes'
    Past = 'past'



class Padej(_Enum):
    '''
    Падеж:
        Nominative - именительный
        Genetive - родительный
        Dative - дательный
        Accusative - винительный
        Instrumental - творительный
        Prepositional - предложный
        PartitiveGenitive - партитив (второй родительный)
        LocalPrepositional - местный (второй предложный)
        Vocative - звательный
    '''
    Nominative = 'nom'
    Genitive = 'gen'
    Dative = 'dat'
    Accusative = 'acc'
    Instrumental = 'ins'
    Prepositional = 'abl'
    PartitiveGenitive = 'part'
    LocalPrepositional = 'loc'
    Vocative = 'voc'


class Number(_Enum):
    '''
    Число:
        Singular - единственное
        Plural - множественное
    '''
    Singular = 'sg'
    Plural = 'pl'



class VerbRepresentation(_Enum):
    '''
    Репрезентация и наклонение глагола:
        Gerund - деепричастие
        Infinitive - инфинитив
        Participle - причастие
        Indicative - изъявительное наклонение
        Imperative - повелительное наклонение
    '''
    Gerund = 'ger'
    Infinitive = 'inf'
    Participle = 'partcp'
    Indicative = 'indic'
    Imperative = 'imper'



class AdjectiveForm(_Enum):
    '''
    Форма прилагательных:
        Short - краткая форма
        Full - полная форма
        Possessive - притяжательное местоимение
    '''
    Short = 'brev'
    Full = 'plen'
    Possessive = 'poss'


class ComparisonDegree(_Enum):
    '''
    Степень сравнения:
        Superb - превосходная
        Comparative - сравнительная
    '''
    Superb = 'supr'
    Comparative = 'comp'



class VerbPerson(_Enum):
    '''
    Лицо глагола:
        First - 1-е лицо
        Second - 2-е лицо
        Third - 3-е лицо
    '''
    First = '1p'
    Second = '2p'
    Third = '3p'



class Gender(_Enum):
    '''
    Род:
        Male - мужской род
        Female - женский род
        Neuter - средний род
    '''
    Male = 'm'
    Female = 'f'
    Neuter = 'n'


class VerbType(_Enum):
    '''
    Вид глагола:
        Perfect - совершенный
        Imperfect - несовершенный
    '''
    Perfect = 'ipf'
    Imperfect = 'pf'



class Pledge(_Enum):
    '''
    Залог:
        Active - действительный залог
        Passive - пассивный залог
    '''
    Active = 'act'
    Passive = 'pass'



class Animateness(_Enum):
    '''
    Одушевленность:
        Animate - одушевленный
        Inanimate - неодушевленный
    '''
    Animate = 'anim'
    Inanimate = 'inan'


class Transitivity(_Enum):
    '''
    Переходность:
        Transitive - переходный глагол
        Intransitive - непереходный глагол
    '''
    Transitive = 'tran'
    Intransitive = 'intr'



class Other(_Enum):
    '''
    Прочие обозначения:
        IntroductionWord - вводное слово
        Geographical - географическое название
        DifficultFormation - образование формы затруднено
        Personal - имя собственное
        Distored - искаженная форма
        CommonFormMaleFemale - общая форма мужского и женского рода
        Obscene - обсценная лексика
        Patronymic - отчество
        Predicative - предикатив
        Informal - разговорная форма
        Rare - редко встречающееся слово
        Abbreviation - абревиатура
        Obsolete - устаревшая форма
        Surname - фамилия
    '''
    IntroductionWord = 'parenth'
    Geographical = 'geo'
    DifficultFormation = 'awkw'
    Personal = 'persn'
    Distorted = 'dist'
    CommonFormMaleFemale = 'mf'
    Obscene = 'obsc'
    Patronymic = 'patrn'
    Predicative = 'praed'
    Informal = 'inform'
    Rare = 'rare'
    Abbreviation = 'abbr'
    Obsolete = 'obsol'
    Surname = 'famn'

