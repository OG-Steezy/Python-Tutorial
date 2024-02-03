import unittest
import steezyfuntions as steezyfuntions

class TestFunctions(unittest.TestCase):
    def test_sort(self):
        testList = [1,5,4,2,8]
        expectedList = [1, 2, 4, 5, 8]

        self.assertEqual(steezyfuntions.sort(testList), expectedList)

    def test_sort_version2(self):
        testList = [1, 0, 5, 4, 2, 8]
        expectedList = [0, 1, 2, 4, 5, 8]

        self.assertEqual(steezyfuntions.sort(testList), expectedList)

    def test_backspace_replacement(self):
        testString = 'abcd~~~'
        expectedString = 'a'
        self.assertEqual(steezyfuntions.backspace_replacement(testString), expectedString)

    def test_is_sorted(self):
        testList = [1,5,4,2,8]
        expectedList = [1, 2, 4, 5, 8]
        self.assertTrue(not steezyfuntions.is_sorted(testList))
        self.assertTrue(steezyfuntions.is_sorted(expectedList))

if __name__ == '__main__':
    unittest.main()

    