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

KoreanDictionaryProvider
'''
__all__ = ['korean_dictionary', 'typo_dictionary', 'correct_typo']

import sys
import os.path
import pkgutil
from collections import namedtuple
from itertools import chain

from fsed.ahocorasick import AhoCorasickTrie

from .KoreanPos import KoreanPos as Pos

import twitter_korean

def pkg_data_lines(*resources, **kwargs):
    return chain.from_iterable(
        pkgutil.get_data(kwargs.get('package', twitter_korean.__name__),
                         os.path.join(kwargs.get('resources_root', twitter_korean.RESOURCES_ROOT),
                                      resource)).decode('utf-8').splitlines()
            for resource in resources)

def read_words(*filenames):
    return set(line for line in pkg_data_lines(*filenames))

korean_dictionary = {
    Pos.Noun: read_words(
      "noun/nouns.txt", "noun/entities.txt", "noun/spam.txt",
      "noun/names.txt", "noun/twitter.txt", "noun/lol.txt",
      "noun/slangs.txt", "noun/company_names.txt",
      "noun/foreign.txt", "noun/geolocations.txt", "noun/profane.txt",
      "substantives/given_names.txt", "noun/kpop.txt", "noun/bible.txt",
      "noun/pokemon.txt", "noun/congress.txt", "noun/wikipedia_title_nouns.txt"
    ),
    Pos.Verb: read_words("verb/verb.txt"),  # TODO: conjugatePredicates
    Pos.Adjective: read_words("adjective/adjective.txt"), # TODO: conjugatePredicates
    Pos.Adverb: read_words("adverb/adverb.txt"),
    Pos.Determiner: read_words("auxiliary/determiner.txt"),
    Pos.Exclamation: read_words("auxiliary/exclamation.txt"),
    Pos.Josa: read_words("josa/josa.txt"),
    Pos.Eomi: read_words("verb/eomi.txt"),
    Pos.PreEomi: read_words("verb/pre_eomi.txt"),
    Pos.Conjunction: read_words("auxiliary/conjunctions.txt"),
    Pos.NounPrefix: read_words("substantives/noun_prefix.txt"),
    Pos.VerbPrefix: read_words("verb/verb_prefix.txt"),
    Pos.Suffix: read_words("substantives/suffix.txt"),
}

def build_typo_trie():
    trie = AhoCorasickTrie()
    for line in pkg_data_lines('typos/typos.txt'):
        before, after = line.split() #decode('utf-8').split()
        trie[before] = after
    return trie

typo_dictionary = build_typo_trie()

def correct_typo(chunk):
    return typo_dictionary.greedy_replace(chunk)
