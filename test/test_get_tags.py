import unittest

import get_tags 

class TestRecover(unittest.TestCase):

    def createSetFromString(self, string, delimiter=" "):
        return set(string.split(delimiter))

    def test_get_tags(self):
        self.assertEqual(
            get_tags.getTags(
                ["zh: 下 了 车 , 进 入 园 明 新 园 .","en: Get off the bus and enter the New Yuan Ming Palace .","wa: 11-12(FUN) 9-8(SEM) 5,6-6(SEM) 1,2[TEN]-1,2(GIS) 7-9(SEM) 4-5(FUN) 8-10(SEM) 3-3,4(TIN) 10-7[DET],11(GIS)"
                ]
            ),
            "GIS:TRA(0:,1:) GIS:TEN(0:,1:) TIN:TRA(2:,3:) FUN:TRA(4:) SEM:TRA(5:) SEM:TRA(5:) SEM:TRA(8:) SEM:TRA(9:) SEM:TRA(7:) GIS:TRA(6:DET,10:) FUN:TRA(11:)") 
        # self.assertEqual(get_tags.getTags(["zh: 微 软 低 调 回 应 Win Vista的SP 1 问 题","en: Microsoft 's Low - Keyed Response to Win Vista 's SP1 Problem","wa: 5,6-6(SEM) 8,9-9,10,11(SEM) 4-5(SEM) 10,11-7[OMN],12(GIS) 7-8(SEM) 3-3(SEM) 1,2-1,2[POS](GIS) -4[COO](NTR)"]), "hoge")
