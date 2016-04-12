import unittest

import recover

class TestRecover(unittest.TestCase):

    def test_recover(self):
        # self.assertEqual(recover.recover("漢 漢 10 漢", "漢 漢10漢"), "漢 漢 10 漢")
        # self.assertEqual(recover.recover("漢 漢 10 漢", "漢 漢 1 0漢"), "漢 漢 10 漢")
        # self.assertEqual(recover.recover("漢 漢 10 20 漢", "漢 漢1 020漢"), "漢 漢 10 20 漢")
        # self.assertEqual(recover.recover("漢 漢 10 20 漢 漢", "漢 漢1 020漢 漢"), "漢 漢 10 20 漢 漢")
        # self.assertEqual(recover.recover("漢 漢 , 漢 , 漢", "漢漢 , 漢 , 漢"), "漢漢 , 漢 , 漢")
        self.assertEqual(
            recover.recover(
                "石 油 输 出 国 家 组 织 秘 书 长 巴 德 里 拒 绝 石 油 消 费 国 要 求 增 加 产 量 的 呼 吁 , 他 说 , 目 前 油 价 高 涨 , 非 基 本 因 素 才 是 主 因 ｡", 
                "石油 输出 国家 组织 秘书长 巴德里 拒绝 石油 消费国 要求 增加 产量 的 呼吁 , 他 说 , 目前 油价 高涨 , 非 基本 因素 才 是 主因 ｡"
            ),
            "石油 输出 国家 组织 秘书长 巴德里 拒绝 石油 消费国 要求 增加 产量 的 呼吁 , 他 说 , 目前 油价 高涨 , 非 基本 因素 才 是 主因 ｡"
        )
