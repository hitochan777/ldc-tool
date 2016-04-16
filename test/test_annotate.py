import unittest

import annotate

class TestRecover(unittest.TestCase):

    def createSetFromString(self, string, delimiter=" "):
        return set(string.split(delimiter))

    def test_annotate(self):
        self.assertEqual(self.createSetFromString(annotate.annotate("SEM:TRA(0) SEM:TRA(1) SEM:TRA(1) SEM:TRA(1)", "漢 漢10漢", "漢 漢 10 漢")), self.createSetFromString("0-0[sure] 1-1[sure]"))
        self.assertEqual(self.createSetFromString(annotate.annotate("SEM:TRA(0) GIS:DEM(1) GIS:DEM(1) GIS:DEM(1)", "漢 漢10漢", "漢 漢 10 漢")), self.createSetFromString("0-0[sure] 1-1[possible]"))
        self.assertEqual(self.createSetFromString(annotate.annotate("SEM:TRA(0) GIS:DEM(1,2) GIS:DEM(1) GIS:DEM(1)", "漢 漢10漢", "漢 漢 10 漢")), self.createSetFromString("0-0[sure] 1-2[possible] 1-1[possible]"))
        self.assertEqual(self.createSetFromString(annotate.annotate("SEM:TRA(0) GIS:DEM(1) SEM:TRA(1) GIS:DEM(1)", "漢 漢10漢", "漢 漢 10 漢")), self.createSetFromString("ignored"))
