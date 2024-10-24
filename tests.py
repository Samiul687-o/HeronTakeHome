import unittest
from main import standardise_description, is_monthly_pattern, identify_recurring_transactions


class TestTransactionProcessing(unittest.TestCase):

    def test_standardise_description(self):
        """
        Unit tests for the standardise_description function to ensure correct removal of month and optional year.
        """
        self.assertEqual(standardise_description("Jan 2021 Acme Corp Salary"), "Acme Corp Salary")

        self.assertEqual(standardise_description("Aug Bonus"), "Bonus")

        self.assertEqual(standardise_description("Acme Corp SalarySep20"), "Acme Corp Salary")

    def test_is_monthly_pattern(self):
        """
        Unit tests for the is_monthly_pattern function to ensure proper detection of monthly patterns.
        """
        # Test case: Regular monthly pattern (same day of each month)
        dates = ["2021-01-01", "2021-02-01", "2021-03-01", "2021-04-01"]
        self.assertTrue(is_monthly_pattern(dates))

        # Test case: Slight day variation (within 2 days)
        dates = ["2021-01-01", "2021-02-02", "2021-03-01", "2021-04-01"]
        self.assertTrue(is_monthly_pattern(dates))

        # Test case: Day variation greater than 2 days
        dates = ["2021-01-01", "2021-02-05", "2021-03-01", "2021-04-01"]
        self.assertFalse(is_monthly_pattern(dates))

    def test_identify_recurring_transactions(self):
        """
        Unit tests for the identify_recurring_transactions function.
        """
        transactions = [
            {"description": "Spotify", "amount": -14.99, "date": "2021-01-29"},
            {"description": "Spotify", "amount": -14.99, "date": "2020-12-29"},
            {"description": "Spotify", "amount": -14.99, "date": "2020-11-29"},
            {"description": "Spotify", "amount": -14.99, "date": "2020-10-29"},
            {"description": "Netflix", "amount": -20.00, "date": "2020-02-15"},
            {"description": "Netflix", "amount": -20.00, "date": "2020-03-14"},
            {"description": "Netflix", "amount": -20.00, "date": "2020-04-16"},
            {"description": "Netflix", "amount": -20.00, "date": "2020-05-15"}
        ]

        # Test case: Detect recurring transactions
        recurring = identify_recurring_transactions(transactions)
        self.assertIn("Spotify", recurring)
        self.assertIn("Netflix", recurring)

        # Test case: Empty transaction list should return empty result
        recurring = identify_recurring_transactions([])
        self.assertEqual(recurring, [])


if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
