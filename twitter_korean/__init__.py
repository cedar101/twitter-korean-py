# -*- coding: utf-8 -*-
import os.path

JAR_DIR = 'data/lib'
RESOURCES_ROOT = os.path.join(JAR_DIR, 'com/twitter/penguin/korean/util')

from .normalizer.KoreanNormalizer import normalize, normalize_coda_n
from .util.KoreanDictionaryProvider import correct_typo

def tokenize(normalized):
    raise NotImplementedError

def stem(tokens):
    raise NotImplementedError

def extractPhrases(tokens, filterSpam=True, enableHashtags=True):
    raise NotImplementedError
