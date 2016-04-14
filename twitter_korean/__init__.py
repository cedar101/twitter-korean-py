RESOURCES_ROOT = 'com.twitter.penguin.korean/src/main/resources/com/twitter/penguin/korean/util'

from .normalizer.KoreanNormalizer import normalize, normalize_coda_n
from .util.KoreanDictionaryProvider import correct_typo
