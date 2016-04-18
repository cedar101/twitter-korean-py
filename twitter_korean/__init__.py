# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
"""
>>> text = "한국어를 처리하는 예시입니닼ㅋㅋㅋㅋㅋ #한국어"
>>> # Normalize
>>> normalized = normalize(text)
>>> print(normalized)
한국어를 처리하는 예시입니다ㅋㅋ #한국어
>>> # Tokenize
>>> tokens = tokenize(normalized)   # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
NotImplementedError: ...
>>> tokens = [('한국어', 'Noun', 0, 3), ('를', 'Josa', 3, 1), (' ', 'Space', 4, 1), ('처리', 'Noun', 5, 2), ('하는', 'Verb', 7, 2), (' ', 'Space', 9, 1), ('예시', 'Noun', 10, 2), ('입니', 'Adjective', 12, 2), ('다', 'Eomi', 14, 1), ('ㅋㅋ', 'KoreanParticle', 15, 2), ('', 'Space', 17, 1), ('#한국어', 'Hashtag', 18, 4)]
>>> # Stemming
>>> stemmed = stem(tokens)  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
NotImplementedError: ...
>>> # Phrase extraction
>>> phrases = extract_phrases(tokens, filter_spam=True, enable_hashtags=True)     # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
NotImplementedError: ...

"""

import os.path

JAR_DIR = 'data/lib'
RESOURCES_ROOT = os.path.join(JAR_DIR, 'com/twitter/penguin/korean/util')

from .normalizer.KoreanNormalizer import normalize, normalize_coda_n
from .util.KoreanDictionaryProvider import correct_typo

def tokenize(normalized):
    raise NotImplementedError

def stem(tokens):
    raise NotImplementedError

def extract_phrases(tokens, filter_spam=True, enable_hashtags=True):
    raise NotImplementedError

if __name__ == "__main__":
    import doctest
    doctest.testmod()
