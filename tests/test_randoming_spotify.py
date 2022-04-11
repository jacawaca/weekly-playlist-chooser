import unittest

import sys, os
testdir = os.path.dirname(__file__)
srcdir = '../'
sys.path.insert(0, os.path.abspath(os.path.join(testdir, srcdir)))

from randoming_spotify import playlist_title_descr

class Test_randoming_spotify(unittest.TestCase):
    def testTitle(self):
        title, descr = playlist_title_descr('syria','hip hop')
        self.assertRegex(title, 'Tydzień [0-9]* - [A-Z][a-z]*')
    def testDescription(self):
        title, descr = playlist_title_descr('syria','hip hop')
        reg = r'Tydzień [0-9]*. Muzyka z gatunku: ([A-Z][a-z]* )*[A-Z][a-z]* z [A-Z][a-z]*.'
        self.assertRegex(descr, reg)
if __name__ == '__main__':
    unittest.main()

