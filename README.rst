twitter-korean-py
=================
.. image:: https://circleci.com/gh/cedar101/twitter-korean-py.svg?style=svg
    :alt: Circle CI Build Status
    :target: https://circleci.com/gh/cedar101/twitter-korean-py
.. image:: https://travis-ci.org/cedar101/twitter-korean-py.svg?branch=master
    :alt: Travis CI Build Status
    :target: https://travis-ci.org/cedar101/twitter-korean-py

**`twitter-korean-py <https://github.com/cedar101/twitter-korean-py>`_**는 *`twitter-korean-text <https://github.com/twitter/twitter-korean-text>`_*의 스칼라 코드를
참고하여 파이썬으로 새로 코딩하여 포팅한 라이브러리입니다.

* 현재는 정규화(normalizer)만 가능하며, 나머지 기능(토큰화, 어근화, 어구 추출)은 아직 구현하지 않았습니다.
* *`JPype <http://jpype.sourceforge.net>`_*를 사용한 래퍼 인터페이스인 *`twkorean <https://github.com/jaepil/twkorean>`_*과는 달리, twitter-korean-text의 스칼라/자바 코드를 사용하지 않은 순수 파이썬(pure-python) 코드입니다.
* 설치 스크립트는 twitter-korean-text의 maven repository에서 JAR 파일을 다운받은 후, 사전 파일만을 압축 해제하여 사용합니다.
  * 이 개념은 twkorean을 참고하였습니다.
  * 파이썬 2.7에서는 *`maven-artifact <https://github.com/hamnis/maven-artifact>`_*라는 툴을 사용하여 maven 없이 설치 가능합니다.
  * 파이썬 3.x에서는 maven(mvn)을 직접 실행해서 다운로드합니다.

Examples
--------
.. code:: pycon

    >>> import twitter_korean
    >>> text = u"한국어를 처리하는 예시입니닼ㅋㅋㅋㅋㅋ #한국어"
    >>> # Normalize
    >>> normalized = twitter_korean.normalize(text)
    >>> print(normalized)
    한국어를 처리하는 예시입니다ㅋㅋ #한국어
    >>> # Tokenize
    >>> tokens = twitter_korean.tokenize(normalized)
    Traceback (most recent call last):
    NotImplementedError: ...
    >>> tokens = [(u'한국어', 'Noun', 0, 3), (u'를', 'Josa', 3, 1), (u' ', 'Space', 4, 1), (u'처리', 'Noun', 5, 2), (u'하는', 'Verb', 7, 2), (u' ', 'Space', 9, 1), (u'예시', 'Noun', 10, 2), (u'입니', 'Adjective', 12, 2), (u'다', 'Eomi', 14, 1), (u'ㅋㅋ', 'KoreanParticle', 15, 2), (u' ', 'Space', 17, 1), (u'#한국어', 'Hashtag', 18, 4)]
    >>> # Stemming
    >>> stemmed = twitter_korean.stem(tokens)
    Traceback (most recent call last):
    NotImplementedError: ...
    >>> # Phrase extraction
    >>> phrases = twitter_korean.extract_phrases(tokens)
    Traceback (most recent call last):
    NotImplementedError: ...
