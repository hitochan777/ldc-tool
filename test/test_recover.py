import unittest

import recover

class TestRecover(unittest.TestCase):

    def test_recover(self):
        self.assertEqual(recover.recover("漢 漢 10 漢", "漢 漢10漢"), "漢 漢 10 漢")
        self.assertEqual(recover.recover("漢 漢 10 漢", "漢 漢 1 0漢"), "漢 漢 10 漢")
        self.assertEqual(recover.recover("漢 漢 10 20 漢", "漢 漢1 020漢"), "漢 漢 10 20 漢")
        self.assertEqual(recover.recover("漢 漢 10 20 漢 漢", "漢 漢1 020漢 漢"), "漢 漢 10 20 漢 漢")
        self.assertEqual(recover.recover("漢 漢 , 漢 , 漢", "漢漢 , 漢 , 漢"), "漢漢 , 漢 , 漢")
        self.assertEqual(recover.recover("我 喜 歓 surface的pro 。", "我 喜歓sur face的pro 。"), "我 喜歓 surface的pro 。")
        self.assertEqual(recover.recover("我 喜 歓 surface的pro 。", "我 喜歓sur face的pro。"), "我 喜歓 surface的pro。")
