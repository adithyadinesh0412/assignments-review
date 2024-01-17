import unittest

from main.substring import print_shortest_substring

class TestSubstring(unittest.TestCase):
    # main string 
    string = "abccdbacca"
    # expected results 
    test_cases = {
        3 : ["acca"],
        4 : ["acca"],
        5 : ["bccdb","cdbac"],
        6 : ["abccdba"],
        7 : ["abccdba"],
        8 : ["not-found"]
    }
    
    def test_substring(self):
        for i in range(3,9):
            result = print_shortest_substring(self.string,i)
            self.assertEqual(result,self.test_cases[i])

