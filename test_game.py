import unittest
from unittest.mock import patch
from io import StringIO
import random
from project import check_winnings, get_slot_machine_spin, print_slot_machine, deposit, get_number_of_lines, get_bet, spin, main


class TestSlotMachineGame(unittest.TestCase):

    # Test for check_winnings function
    def test_check_winnings(self):
        columns = [['A', 'A'], ['A', 'A'], ['A', 'A']]  # All lines winning
        lines = 2
        bet = 5
        values = {'A': 10}
        winning_lines, winnings = check_winnings(columns, lines, bet, values)
        self.assertEqual(winning_lines, [1, 2])
        # 2 lines * 10 (symbol value) * 5 (bet)
        self.assertEqual(winnings, 100)

    def test_check_winnings_no_win(self):
        # Only the second line matches
        columns = [['A', 'B'], ['A', 'B'], ['C', 'B']]
        lines = 2
        bet = 5
        values = {'A': 10, 'B': 5, 'C': 2}
        winning_lines, winnings = check_winnings(columns, lines, bet, values)
        self.assertEqual(winning_lines, [2])  # Correct expected output
        self.assertEqual(winnings, 25)  # Correct winnings: 5 * 5 (bet)

    # Test for get_slot_machine_spin function
    @patch('random.choice')
    def test_get_slot_machine_spin(self, mock_choice):
        mock_choice.side_effect = ['A', 'B', 'C', 'A', 'B', 'C']
        rows = 2
        cols = 3
        symbols = {'A': 2, 'B': 2, 'C': 2}
        result = get_slot_machine_spin(rows, cols, symbols)
        expected = [['A', 'B'], ['C', 'A'], ['B', 'C']]
        self.assertEqual(result, expected)

    # Test for print_slot_machine function
    def test_print_slot_machine(self):
        columns = [['A', 'B'], ['C', 'D'], ['E', 'F']]
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            print_slot_machine(columns)
        output = captured_output.getvalue()
        expected_output = "A | C | E\nB | D | F\n"
        self.assertEqual(output, expected_output)

    # Test for deposit function
    @patch('builtins.input', side_effect=['abc', '-10', '100'])
    def test_deposit(self, mock_input):
        result = deposit()
        self.assertEqual(result, 100)

    # Test for get_number_of_lines function
    @patch('builtins.input', side_effect=['5', '2'])
    def test_get_number_of_lines(self, mock_input):
        global MAX_LINES
        MAX_LINES = 3
        result = get_number_of_lines()
        self.assertEqual(result, 2)

    # Test for get_bet function
    @patch('builtins.input', side_effect=['abc', '50'])
    def test_get_bet(self, mock_input):
        global MIN_BET, MAX_BET
        MIN_BET = 10
        MAX_BET = 50
        result = get_bet()
        self.assertEqual(result, 50)  # Adjusted to match the second input


if __name__ == '__main__':
    unittest.main()
