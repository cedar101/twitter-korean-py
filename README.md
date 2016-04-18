[![Circle CI](https://circleci.com/gh/cedar101/twitter-korean-py.svg?style=svg)](https://circleci.com/gh/cedar101/twitter-korean-py)
[![Build Status](https://travis-ci.org/cedar101/twitter-korean-py.svg?branch=master)](https://travis-ci.org/cedar101/twitter-korean-py)
twitter-korean-py
=================
Python port to the normalizer in [twitter-korean-text](https://github.com/twitter/twitter-korean-text)

[twitter-korean-text](https://github.com/twitter/twitter-korean-text)의 정규화 기능을
파이썬으로 포팅했습니다. 나머지 기능(토큰화, 어근화, 어구 추출)은 아직 지원하지 않습니다.

```python
>>> import twitter_korean
>>> text = "한국어를 처리하는 예시입니닼ㅋㅋㅋㅋㅋ #한국어"
>>> # Normalize
>>> normalized = twitter_korean.normalize(text)
>>> print(normalized)
한국어를 처리하는 예시입니다ㅋㅋ #한국어
>>> # Tokenize
>>> tokens = twitter_korean.tokenize(normalized)   # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
NotImplementedError: ...
>>> tokens = [('한국어', 'Noun', 0, 3), ('를', 'Josa', 3, 1), (' ', 'Space', 4, 1), ('처리', 'Noun', 5, 2), ('하는', 'Verb', 7, 2), (' ', 'Space', 9, 1), ('예시', 'Noun', 10, 2), ('입니', 'Adjective', 12, 2), ('다', 'Eomi', 14, 1), ('ㅋㅋ', 'KoreanParticle', 15, 2), (' ', 'Space', 17, 1), ('#한국어', 'Hashtag', 18, 4)]
>>> # Stemming
>>> stemmed = twitter_korean.stem(tokens)  # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
NotImplementedError: ...
>>> # Phrase extraction
>>> phrases = twitter_korean.extract_phrases(tokens, filter_spam=True, enable_hashtags=True)     # doctest: +IGNORE_EXCEPTION_DETAIL
Traceback (most recent call last):
NotImplementedError: ...

```
