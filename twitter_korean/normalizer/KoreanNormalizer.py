# -*- encoding: utf-8 -*-
'''
 *
 * Python port of Twitter Korean Text - Scala library to process Korean text
 *
 * Copyright 2016 Kim, Baeg-il.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *

KoreanNormalizer: Normalize Korean colloquial text
'''
from __future__ import unicode_literals, print_function

import re
from collections import namedtuple
from korean import hangul

from ..util.KoreanPos import KoreanPos as Pos
from ..util.KoreanDictionaryProvider import korean_dictionary, correct_typo

__all__ = ['normalize', 'normalize_coda_n', 'HangulChar']

EXTENTED_KOREAN_REGEX = re.compile(r"([ㄱ-ㅣ가-힣]+)", re.U)
KOREAN_TO_NORMALIZE_REGEX = re.compile(r"([가-힣]+)(ㅋ+|ㅎ+|[ㅠㅜ]+)", re.U)
REPEATING_CHAR_REGEX = re.compile(r"(.)\1{2,}|[ㅠㅜ]{2,}", re.U)
REPEATING_2CHAR_REGEX = re.compile(r"(..)\1{2,}", re.U)
WHITESPACE_REGEX = re.compile(r"\s+", re.U)

CODA_N_EXCEPTION = set("은는운인텐근른픈닌든던")

class HangulChar(namedtuple('HangulChar', 'onset vowel coda')):
    __slots__ = ()
    def __new__(cls, onset, vowel, coda=''):
        'Create a new instance of HangulChar'
        return super(cls, HangulChar).__new__(cls, onset, vowel, coda)

    def __str__(self):
        '풀어쓰기 표기'
        return '{self.__class__.__name__}({self.onset}{self.vowel}{self.coda})'.format(self=self)

    @classmethod
    def decompose(cls, hc):
        return cls._make(hangul.split_char(hc))

    def compose(self):
        return hangul.join_char(self)


def normalize(s):
    '''
    Normalize Korean CharSequence text
    * ex) 하댘ㅋㅋㅋ -> 하대, 머구뮤ㅠㅠㅠ -> 머굼, 하즤 -> 하지

    @param input input CharSequence
    @return normalized CharSequence
    '''
    return EXTENTED_KOREAN_REGEX.sub(lambda m: normalize_korean_chunk(m.group(0)),
                                     s)

def normalize_korean_chunk(s):
    # Normalize endings: 안됔ㅋㅋㅋ -> 안돼ㅋㅋ
    ending_normalized = KOREAN_TO_NORMALIZE_REGEX.sub(process_normalization_candidate,
                                                      s)

    # Normalize repeating chars: ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ -> ㅋㅋ
    exclamation_normalized = REPEATING_CHAR_REGEX.sub(lambda m: m.group(0)[:2],
                                                      ending_normalized)

    # Normalize repeating chars: 훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍 -> 훌쩍훌쩍
    repeating_normalized = REPEATING_2CHAR_REGEX.sub(lambda m: m.group(0)[:4],
                                                     exclamation_normalized)

    # Coda normalization (명사 + ㄴ 첨가 정규화): 소린가 -> 소리인가
    coda_n_normalized = normalize_coda_n(repeating_normalized)
    # Typo correction: 하겟다 -> 하겠다
    typo_corrected = correct_typo(coda_n_normalized)
    # Spaces, tabs, new lines are replaced with a single space.
    return WHITESPACE_REGEX.sub(typo_corrected, " ")

def normalize_coda_n(chunk):
    if len(chunk) < 2:
        return chunk

    last_two = chunk[-2:]
    last = chunk[-1]
    last_two_head = last_two[0]

    # Exceptional cases
    if (chunk in korean_dictionary[Pos.Noun] or
        chunk in korean_dictionary[Pos.Conjunction] or
        chunk in korean_dictionary[Pos.Adverb] or
        last_two in korean_dictionary[Pos.Noun] or
        last_two_head < '가' or last_two_head > '힣' or
        last_two_head in CODA_N_EXCEPTION):
        return chunk

    hc = HangulChar.decompose(last_two_head)

    new_head = ''.join((chunk[:-2],
                        HangulChar(hc.onset, hc.vowel).compose()))

    if (hc.coda == 'ㄴ' and
        last in ('데', '가', '지') and
        new_head in korean_dictionary[Pos.Noun]):
        mid = "은" if hc.vowel == 'ㅡ' else "인"
        return new_head + mid + last
    return chunk

def process_normalization_candidate(m):
    chunk = m.group(1)
    to_normalize = m.group(2)

    normalized_chunk = (
    chunk
        if (chunk in korean_dictionary[Pos.Noun] or
            chunk[-1] in korean_dictionary[Pos.Eomi] or
            chunk[-2:] in korean_dictionary[Pos.Eomi])
        else
            normalize_emotion_attached_chunk(chunk, to_normalize)
    )
    return normalized_chunk + to_normalize

def normalize_emotion_attached_chunk(s, to_normalize):
    # Implemented using simple imperative statements
    # instead of pattern matching in the functional language Scala :)

    def second_to_last_decomposed(si):
        if si:
            hc = HangulChar.decompose(si[-1])
            if hc.coda == '':
                return hc
        return None

    init = s[0:-1]
    hc = second_to_last_decomposed(init)
    o, v, c = HangulChar.decompose(s[-1])
    if c in ('ㅋ', 'ㅎ'):
        return ''.join((init, HangulChar(o, v).compose()))
    if c == '' and hc and v == to_normalize[0] and o in hangul.FINALS:
        return ''.join((init[:-1], HangulChar(hc.onset, hc.vowel, o).compose()))
    return s
