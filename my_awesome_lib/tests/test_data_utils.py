import os
import unittest
from my_awesome_lib import data_utils


class TestDataUtils(unittest.TestCase):
    def test_transform_data(self):
        data = [1, 2, 3]
        result = data_utils.transform_data(data, lambda x: x * 2)
        self.assertEqual(result, [2, 4, 6])

    def test_read_write_csv(self):
        test_file = 'test.csv'
        data = [['col1', 'col2'], ['1', '2']]
        data_utils.write_csv(test_file, data)
        read_data = data_utils.read_csv(test_file)
        self.assertEqual(read_data, data)
        os.remove(test_file)


if __name__ == '__main__':
    unittest.main()
