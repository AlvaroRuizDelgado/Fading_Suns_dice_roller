from roll import roll
import unittest
from unittest import mock   # pylint: disable=E0611

class TestRoll(unittest.TestCase):

    examples_d20 = [ 
        {'die_range': 20, 'dice_number': 1, 'difficulty': 10, 'die_roll': 10, 'victory_points': 6, 'victory_dice': 6},
        {'die_range': 20, 'dice_number': 1, 'difficulty': 10, 'die_roll': 11, 'victory_points': 0, 'victory_dice': 0},
        {'die_range': 20, 'dice_number': 1, 'difficulty': 10, 'die_roll': 20, 'victory_points': 0, 'victory_dice': 0},
        {'die_range': 20, 'dice_number': 1, 'difficulty': 15, 'die_roll': 14, 'victory_points': 4, 'victory_dice': 4},
        {'die_range': 20, 'dice_number': 1, 'difficulty': 8, 'die_roll': 12, 'victory_points': 0, 'victory_dice': 0},
        {'die_range': 20, 'dice_number': 1, 'difficulty': 27, 'die_roll': 15, 'victory_points': 5, 'victory_dice': 8},
        {'die_range': 20, 'dice_number': 1, 'difficulty': 20, 'die_roll': 19, 'victory_points': 0, 'victory_dice': 0},
        {'die_range': 20, 'dice_number': 1, 'difficulty': 20, 'die_roll': 20, 'victory_points': 0, 'victory_dice': 0}
    ]

    examples_d6 = [ 
        {'die_range': 6, 'dice_number': 7, 'difficulty': 4, 'die_roll': 1, 'success_rolls': 7},
        {'die_range': 6, 'dice_number': 6, 'difficulty': 4, 'die_roll': 2, 'success_rolls': 6},
        {'die_range': 6, 'dice_number': 4, 'difficulty': 4, 'die_roll': 3, 'success_rolls': 4},
        {'die_range': 6, 'dice_number': 5, 'difficulty': 4, 'die_roll': 4, 'success_rolls': 5},
        {'die_range': 6, 'dice_number': 8, 'difficulty': 4, 'die_roll': 5, 'success_rolls': 0},
        {'die_range': 6, 'dice_number': 2, 'difficulty': 4, 'die_roll': 6, 'success_rolls': 0},
        {'die_range': 6, 'dice_number': 8, 'difficulty': 2, 'die_roll': 3, 'success_rolls': 0},
        {'die_range': 6, 'dice_number': 2, 'difficulty': 6, 'die_roll': 6, 'success_rolls': 2}
    ]

    def setUp(self):
        pass

    def test_help(self):
        with self.assertRaises(SystemExit) as cm:
            roll([])
        self.assertEqual(0, cm.exception.code)
        with self.assertRaises(SystemExit) as cm:
            roll(['-h'])
        self.assertEqual(0, cm.exception.code)
        with self.assertRaises(SystemExit) as cm:
            roll(['--help'])
        self.assertEqual(0, cm.exception.code)

    def test_wrong_input(self):
        with self.assertRaises(SystemExit) as cm:
            roll(['d15', 10])
        self.assertEqual(1, cm.exception.code)

    @mock.patch('roll.randint')
    def test_d20_working_mock(self, mock_randint):
        mock_randint.return_value = 10
        roll(['d20', 10])
        self.assertTrue(mock_randint.called)

    @mock.patch('roll.randint')
    def test_d20_test(self, mock_randint):
        for expectation in self.examples_d20:
            mock_randint.return_value = expectation['die_roll']
            actual = roll(['d20', expectation['difficulty']])
            test_result(self, expectation, actual)

    @mock.patch('roll.randint')
    def test_d6_working_mock(self, mock_randint):
        mock_randint.return_value = 10
        roll(['d6', 7])
        self.assertTrue(mock_randint.called)

    @mock.patch('roll.randint')
    def test_d6_test(self, mock_randint):
        for expectation in self.examples_d6:
            mock_randint.return_value = expectation['die_roll']
            actual = roll(['d6', expectation['dice_number'], '-d', expectation['difficulty']])
            test_result(self, expectation, actual)

def test_result(self, expectation, actual):
    self.assertEqual( expectation['die_range'],   actual['die_range'] )
    self.assertEqual( expectation['dice_number'], actual['dice_number'] )
    self.assertEqual( expectation['difficulty'],  actual['difficulty'] )
    self.assertEqual( expectation['die_roll'],    actual['die_roll'] )
    if actual['die_range'] == 20:
        self.assertEqual( expectation['victory_points'], actual['victory_points'] )
        self.assertEqual( expectation['victory_dice'],   actual['victory_dice'] )
    elif actual['die_range'] == 6:
        self.assertEqual( expectation['success_rolls'], actual['success_rolls'] )

if __name__ == '__main__':
    unittest.main()
