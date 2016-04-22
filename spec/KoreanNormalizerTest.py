#!/usr/bin/env mamba
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
'''
from twitter_korean import normalize, normalize_coda_n, correct_typo

with context('Test KoreanNormalizer'):
    with it("normalize should normalize ㅋㅋ ㅎㅎ ㅠㅜ chunks"):
        assert(normalize(
            u"안됔ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ내 심장을 가격했엌ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
            == u"안돼ㅋㅋ내 심장을 가격했어ㅋㅋ")
        assert(normalize(u"무의식중에 손들어버려섴ㅋㅋㅋㅋ") == u"무의식중에 손들어버려서ㅋㅋ")
        assert(normalize(u"기억도 나지아낳ㅎㅎㅎ") == u"기억도 나지아나ㅎㅎ")
        assert(normalize(u"근데비싸서못머구뮤ㅠㅠ") == u"근데비싸서못먹음ㅠㅠ")

        assert(normalize(u"미친 존잘니뮤ㅠㅠㅠㅠ") == u"미친 존잘님ㅠㅠ")
        assert(normalize(u"만나무ㅜㅜㅠ") == u"만남ㅜㅜ")
        assert(normalize(u"가루ㅜㅜㅜㅜ") == u"가루ㅜㅜ")
        assert(normalize(u"최지우ㅜㅜㅜㅜ") == u"최지우ㅜㅜ")

        assert(normalize(u"유성우ㅠㅠㅠ") == u"유성우ㅠㅠ")
        assert(normalize(u"ㅎㅎㅎㅋㅋ트위터ㅋㅎㅋ월드컵ㅠㅜㅠㅜㅠ")
               == u"ㅎㅎㅋㅋ트위터ㅋㅎㅋ월드컵ㅠㅜ")

        assert(normalize(u"예뿌ㅠㅠ") == u"예뻐ㅠㅠ")
        assert(normalize(u"고수야고수ㅠㅠ") == u"고수야고수ㅠㅠ")

    with it("normalize should normalize repeated chunks") :
        assert(normalize(u"땡큐우우우우우우") == u"땡큐우우")
        assert(normalize(u"구오오오오오오오오옹오오오") == u"구오오옹오오")

    with it("normalize should normalize repeated 2-letters") :
        assert(normalize(u"훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍훌쩍") == u"훌쩍훌쩍")
        assert(normalize(u"ㅋㅎㅋㅎㅋㅎㅋㅎㅋㅎㅋㅎ") == u"ㅋㅎㅋㅎ")

    with it("normalize should not normalize non-Korean chunks") :
        assert(normalize(u"http://11111.cccccom soooooooo !!!!!!!!!!!!!!!") ==
            "http://11111.cccccom soooooooo !!!!!!!!!!!!!!!")

    with it("normalize should have correctTypo integrated") :
        assert(normalize(u"가쟝 용기있는 사람이 머굼 되는거즤")
               == u"가장 용기있는 사람이 먹음 되는거지")

    with it("normalize should have normalize_coda_n integrated") :
        assert(normalize(u"오노딘가") == u"오노디인가")
        assert(normalize(u"관곈지") == u"관계인지")
        assert(normalize(u"생각하는건데") == u"생각하는건데")

    with it("normalize_coda_n should normalize coda N nouns correctly") :
        assert(normalize_coda_n(u"오노딘가") == u"오노디인가")
        assert(normalize_coda_n(u"소린가") == u"소리인가")
        assert(normalize_coda_n(u"쵸킨데") == u"쵸킨데")  # Unknown noun

    with it("normalize_coda_n should not normalize if the input is known in the dictionary") :
        assert(normalize_coda_n(u"누군가") == u"누군가")
        assert(normalize_coda_n(u"군가") == u"군가")

    with it("normalize_coda_n should not normalize if the input is an adjective or a verb") :
        assert(normalize_coda_n(u"가는건데") == u"가는건데")
        assert(normalize_coda_n(u"곤란한데") == u"곤란한데")
        assert(normalize_coda_n(u"생각하는건데") == u"생각하는건데")

    with it("correct_typo should correct typos") :
        #assert(correct_typo(u"하겟다") == u"하겠다")
        assert(correct_typo(u"가쟝 용기있는 사람이 머굼 되는거즤")
               == u"가장 용기있는 사람이 먹음 되는거지")
        assert(correct_typo(u"만듀 먹것니? 먹겄서? 먹즤?")
               == u"만두 먹겠니? 먹겠어? 먹지?")
