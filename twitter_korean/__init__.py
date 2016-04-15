# -*- coding: utf-8 -*-

RESOURCES_ROOT = 'com.twitter.penguin.korean/src/main/resources/com/twitter/penguin/korean/util'
JAR_DIR = 'data/lib'

from .normalizer.KoreanNormalizer import normalize, normalize_coda_n
from .util.KoreanDictionaryProvider import correct_typo

def tokenize(normalized):
    raise NotImplementedError

def stem(tokens):
    raise NotImplementedError

def extractPhrases(tokens, filterSpam=True, enableHashtags=True):
    raise NotImplementedError
