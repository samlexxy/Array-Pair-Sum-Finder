from main import get_unique_pairs
import unittest

class TestGetUniquePairs(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(get_unique_pairs([]), [])

    def test_no_duplicate_sums(self):
        # Tes with an empty array
        array = [1, 2, 3]
        self.assertEqual(get_unique_pairs(array), [])

    def test_with_duplicate_sums(self):
        # Test with an array that produces duplicate sums
        array = [6, 4, 12, 10, 22, 54, 32, 42, 21, 11]
        expected_output = [
            "Pairs : ( 4, 12) ( 6, 10) have sum : 16",
            "Pairs : ( 10, 22) ( 21, 11) have sum : 32",
            "Pairs : ( 12, 21) ( 22, 11) have sum : 33",
            "Pairs : ( 22, 21) ( 32, 11) have sum : 43",
            "Pairs : ( 32, 21) ( 42, 11) have sum : 53",
            "Pairs : ( 12, 42) ( 22, 32) have sum : 54",
            "Pairs : ( 10, 54) ( 22, 42) have sum : 64",
        ]
        self.assertEqual(get_unique_pairs(array), expected_output)

    def test_with_a_smaller_array(self):
        # Test with a smaller array to correctness
        array = [4, 23, 65, 67, 24, 12, 86]
        expected_output = ["Pairs : ( 4, 86) ( 23, 67) have sum : 90"]
        self.assertEqual(get_unique_pairs(array), expected_output)

if __name__ == "__main__":
    unittest.main()
