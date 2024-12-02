import unittest
from io import StringIO
import sys
from app import datetime

def determine_quarter(date_str):
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d')
        month = date.month
        if 1 <= month <= 3:
            return f"Дата {date_str} відноситься до 1-го кварталу."
        elif 4 <= month <= 6:
            return f"Дата {date_str} відноситься до 2-го кварталу."
        elif 7 <= month <= 9:
            return f"Дата {date_str} відноситься до 3-го кварталу."
        elif 10 <= month <= 12:
            return f"Дата {date_str} відноситься до 4-го кварталу."
    except ValueError:
        return "Невірний формат дати. Будь ласка, використовуйте формат 'YYYY-MM-DD'."

class TestDetermineQuarter(unittest.TestCase):
    def test_valid_quarters(self):
        self.assertEqual(determine_quarter('2024-01-01'), "Дата 2024-01-01 відноситься до 1-го кварталу.")
        self.assertEqual(determine_quarter('2024-04-01'), "Дата 2024-04-01 відноситься до 2-го кварталу.")
        self.assertEqual(determine_quarter('2024-07-01'), "Дата 2024-07-01 відноситься до 3-го кварталу.")
        self.assertEqual(determine_quarter('2024-10-01'), "Дата 2024-10-01 відноситься до 4-го кварталу.")

    def test_invalid_date_format(self):
        self.assertEqual(determine_quarter('01-01-2024'), "Невірний формат дати. Будь ласка, використовуйте формат 'YYYY-MM-DD'.")
        self.assertEqual(determine_quarter('2024/01/01'), "Невірний формат дати. Будь ласка, використовуйте формат 'YYYY-MM-DD'.")
        self.assertEqual(determine_quarter('invalid_date'), "Невірний формат дати. Будь ласка, використовуйте формат 'YYYY-MM-DD'.")

    def test_edge_cases(self):
        self.assertEqual(determine_quarter('2024-03-31'), "Дата 2024-03-31 відноситься до 1-го кварталу.")
        self.assertEqual(determine_quarter('2024-06-30'), "Дата 2024-06-30 відноситься до 2-го кварталу.")
        self.assertEqual(determine_quarter('2024-09-30'), "Дата 2024-09-30 відноситься до 3-го кварталу.")
        self.assertEqual(determine_quarter('2024-12-31'), "Дата 2024-12-31 відноситься до 4-го кварталу.")

    def test_nonexistent_dates(self):
        self.assertEqual(determine_quarter('2024-02-30'), "Невірний формат дати. Будь ласка, використовуйте формат 'YYYY-MM-DD'.")

    def test_autotest_input(self):
        inputs = [
            '2024-01-01', '2024-04-01', '2024-07-01', '2024-10-01',
            '01-01-2024', '2024/01/01', 'invalid_date',
            '2024-03-31', '2024-06-30', '2024-09-30', '2024-12-31',
            '2024-02-30'
        ]
        expected_outputs = [
            "Дата 2024-01-01 відноситься до 1-го кварталу.",
            "Дата 2024-04-01 відноситься до 2-го кварталу.",
            "Дата 2024-07-01 відноситься до 3-го кварталу.",
            "Дата 2024-10-01 відноситься до 4-го кварталу.",
            "Невірний формат дати. Будь ласка, використовуйте формат 'YYYY-MM-DD'.",
            "Невірний формат дати. Будь ласка, використовуйте формат 'YYYY-MM-DD'.",
            "Невірний формат дати. Будь ласка, використовуйте формат 'YYYY-MM-DD'.",
            "Дата 2024-03-31 відноситься до 1-го кварталу.",
            "Дата 2024-06-30 відноситься до 2-го кварталу.",
            "Дата 2024-09-30 відноситься до 3-го кварталу.",
            "Дата 2024-12-31 відноситься до 4-го кварталу.",
            "Невірний формат дати. Будь ласка, використовуйте формат 'YYYY-MM-DD'."
        ]
        
        for date_input, expected_output in zip(inputs, expected_outputs):
            with self.subTest(date_input=date_input):
                self.assertEqual(determine_quarter(date_input), expected_output)

if __name__ == '__main__':
    unittest.main()
