import unittest
import os
from CSP_6_02_reading_files import toString, longestLine, toBinary


class TestFileFunctions(unittest.TestCase):

    def setUp(self):
        """Creates temporary files to use for the tests."""
        self.txt_name = "temp_test.txt"
        self.bin_name = "temp_bits.txt"

        with open(self.txt_name, "w") as f:
            f.write("Short line\nThis is the longest line in the file\nTiny")

        with open(self.bin_name, "w") as f:
            f.write("0110100100101010101")

    def tearDown(self):
        """Deletes the temporary files after the tests finish."""
        for file in [self.txt_name, self.bin_name]:
            if os.path.exists(file):
                os.remove(file)

    def test_toString(self):
        result = toString(self.txt_name)
        self.assertIn("Short line", result)
        self.assertIn("longest line", result)

    def test_longestLine(self):
        # Testing if it correctly identifies the longest string
        expected = "This is the longest line in the file"
        self.assertEqual(longestLine(self.txt_name), expected)

    def test_toBinary(self):
        # Testing if it breaks the string into 8-character chunks (bytes)
        expected = ['01101001', '00101010', '101']
        self.assertEqual(toBinary(self.bin_name), expected)


if __name__ == "__main__":
    unittest.main()