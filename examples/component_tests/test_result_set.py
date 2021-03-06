import unittest

from constantcontact import Result_Set

class Test_Result_Set(unittest.TestCase):
    def test_resultset(self):
        resultset = Result_Set({'meta': {'pagination': {'next_link': 'Some url'}}, 'results': ['result1', 'result2']})

        self.assertEqual(resultset.get_next_page(), 'Some url')
        self.assertEqual(len(resultset.get_set()), 2)
        self.assertEqual(resultset.get_item(0), 'result1')
        self.assertEqual(resultset.get_set_type(), str)

        resultset.add_item('result3')
        
        self.assertEqual(len(resultset.get_set()), 3)

        resultset.remove_item(1)

        self.assertEqual(resultset.get_item(1), 'result3')

        resultset.clear_result_set()

        self.assertEqual(len(resultset.get_set()), 0)

if __name__ == '__main__':
    unittest.main()
