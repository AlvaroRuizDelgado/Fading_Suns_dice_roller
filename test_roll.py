from roll import roll
 
import unittest
from unittest import mock

class TestRoll(unittest.TestCase):


    def setUp(self):
        pass
 
    @mock.patch('roll.randint')
    def test_d20_pass(self, mock_randint):
        mock_randint.return_value = 10
        roll(['d20', 10])
        self.assertTrue(mock_randint.called)
        self.assertEqual( roll.difficulty, 10 )
        #self.assertEqual( roll.victory_points, 3 )
 
#    def test_d6(self):
#        self.assertEqual( roll(['d6',3]), [1, 2, 3])
 
if __name__ == '__main__':
    unittest.main()
