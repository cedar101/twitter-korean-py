# -*- encoding: utf-8 -*-
'''
 *
 * Twitter Korean Text - Scala library to process Korean text
 *
 * Copyright 2014 Twitter, Inc.
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
'''
from __future__ import unicode_literals

from twitter_korean import normalize, normalize_coda_n, correct_typo

with context(b'Test KoreanNormalizer'):
    with it(b"normalize should normalize ㅋㅋ ㅎㅎ ㅠㅜ chunks") :
        assert(normalize(
            "안됔ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ내 심장을 가격했엌ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
            == "안돼ㅋㅋ내 심장을 가격했어ㅋㅋ")
        assert(normalize("무의식중에 손들어버려섴ㅋㅋㅋㅋ") == "무의식중에 손들어버려서ㅋㅋ")
        assert(normalize("기억도 나지아낳ㅎㅎㅎ") == "기억도 나지아나ㅎㅎ")
        assert(normalize("근데비싸서못머구뮤ㅠㅠ") == "근데비싸서못먹음ㅠㅠ")

        assert(normalize("미친 존잘니뮤ㅠㅠㅠㅠ") == "미친 존잘님ㅠㅠ")
        assert(normalize("만나무ㅜㅜㅠ") == "만남ㅜㅜ")
        assert(normalize("가루ㅜㅜㅜㅜ") == "가루ㅜㅜ")
        assert(normalize("최지우ㅜㅜㅜㅜ") == "최지우ㅜㅜ")

        assert(normalize("유성우ㅠㅠㅠ") == "유성우ㅠㅠ")
        assert(normalize("ㅎㅎㅎㅋㅋ트위터ㅋㅎㅋ월드컵ㅠㅜㅠㅜㅠ")
               == "ㅎㅎㅋㅋ트위터ㅋㅎㅋ월드컵ㅠㅜ")

        assert(normalize("예뿌ㅠㅠ") == "예뻐ㅠㅠ")
        assert(normalize("고수야고수ㅠㅠ") == "고수야고수ㅠㅠ")

    with it(b"normalize should normalize repeated chunks") :
        assert(normalize("땡큐우우우우우우") == "땡큐우우")
        assert(normalize("구오오오오오오오오옹오오오") == "구오오옹오오")

    with it(b"normalize should normalize repeated 2-letters") :
        assert(normalize("훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍") == "훌쩍훌쩍")
        assert(normalize("ㅋㅎㅋㅎㅋㅎㅋㅎㅋㅎㅋㅎ") == "ㅋㅎㅋㅎ")

    with it(b"normalize should not normalize non-Korean chunks") :
        assert(normalize("http://11111.cccccom soooooooo !!!!!!!!!!!!!!!") ==
            "http://11111.cccccom soooooooo !!!!!!!!!!!!!!!")

    with it(b"normalize should have correctTypo integrated") :
        assert(normalize("가쟝 용기있는 사람이 머굼 되는거즤")
               == "가장 용기있는 사람이 먹음 되는거지")

    with it(b"normalize should have normalize_coda_n integrated") :
        assert(normalize("오노딘가") == "오노디인가")
        assert(normalize("관곈지") == "관계인지")
        assert(normalize("생각하는건데") == "생각하는건데")

    with it(b"normalize_coda_n should normalize coda N nouns correctly") :
        assert(normalize_coda_n("오노딘가") == "오노디인가")
        assert(normalize_coda_n("소린가") == "소리인가")
        assert(normalize_coda_n("쵸킨데") == "쵸킨데")  # Unknown noun

    with it(b"normalize_coda_n should not normalize if the input is known in the dictionary") :
        assert(normalize_coda_n("누군가") == "누군가")
        assert(normalize_coda_n("군가") == "군가")

    with it(b"normalize_coda_n should not normalize if the input is an adjective or a verb") :
        assert(normalize_coda_n("가는건데") == "가는건데")
        assert(normalize_coda_n("곤란한데") == "곤란한데")
        assert(normalize_coda_n("생각하는건데") == "생각하는건데")

    with it(b"correct_typo should correct typos") :
        #assert(correct_typo("하겟다") == "하겠다")
        assert(correct_typo("가쟝 용기있는 사람이 머굼 되는거즤")
               == "가장 용기있는 사람이 먹음 되는거지")
        assert(correct_typo("만듀 먹것니? 먹겄서? 먹즤?")
               == "만두 먹겠니? 먹겠어? 먹지?")
