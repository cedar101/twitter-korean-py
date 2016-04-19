# -*- coding: utf-8 -*-
import os.path

#JAR_DIR = 'data/lib'
#RESOURCES_ROOT = os.path.join(JAR_DIR, 'com/twitter/penguin/korean/util')
RESOURCES_ROOT = 'com/twitter/penguin/korean/util'

# lazy imports

def normalize(s):
    from .normalizer.KoreanNormalizer import normalize
    return normalize(s)

def normalize_coda_n(chunk):
    from .normalizer.KoreanNormalizer import normalize_coda_n
    return normalize_coda_n(chunk)

def correct_typo(chunk):
    from .util.KoreanDictionaryProvider import correct_typo
    return correct_typo(chunk)

# not implemented

def tokenize(normalized):
    raise NotImplementedError

def stem(tokens):
    raise NotImplementedError

def extract_phrases(tokens, filter_spam=True, enable_hashtags=True):
    raise NotImplementedError
