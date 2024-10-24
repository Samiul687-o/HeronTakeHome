import json
import re
import logging
from datetime import datetime
from collections import defaultdict
from typing import List, Dict, Optional

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

Transaction = Dict[str, Optional[str]]

DATE_FORMAT = "%Y-%m-%d"


def standardise_description(description: str) -> str:
    """
    Standardises the transaction description by removing the month and optional year.
    """
    regex = r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)(?:[-/ ]?\d{2,4})?'
    return re.sub(regex, '', description).strip()


def is_monthly_pattern(dates: List[str]) -> bool:
    """
    Checks if the dates follow a consistent monthly pattern.

    """
    try:
        parsed_dates = sorted([datetime.strptime(date, DATE_FORMAT) for date in dates])
    except ValueError as e:
        logging.error(f"Date parsing error: {e}")
        return False

    monthly_differences = [(parsed_dates[i] - parsed_dates[i - 1]).days for i in range(1, len(parsed_dates))]

    return all(27 <= diff <= 33 for diff in monthly_differences)


def identify_recurring_transactions(transactions: List[Transaction]) -> List[str]:
    """
    Identifies recurring transactions by grouping them by description and checking for a monthly pattern.

    """
    grouped_transactions = defaultdict(list)

    for transaction in transactions:
        description = transaction.get('description')
        date = transaction.get('date')

        if not description or not date:
            logging.warning(f"Skipping transaction with missing description or date: {transaction}")
            continue

        standardised_desc = standardise_description(description)
        grouped_transactions[standardised_desc].append(transaction)

    recurring_transactions = []

    for description, transaction_group in grouped_transactions.items():
        if len(transaction_group) < 3:
            continue
        dates = [t['date'] for t in transaction_group if t.get('date')]
        if is_monthly_pattern(dates):
            recurring_transactions.append(description)

    return recurring_transactions


def load_transactions_from_file(file_path: str) -> List[Transaction]:
    """
    Loads transactions from a given JSON file.

    Used only for testing purposes.

    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data.get('transactions', [])
    except FileNotFoundError as e:
        logging.error(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError as e:
        logging.error(f"Error decoding JSON from file {file_path}: {e}")
        return []


def main(file_path: str):
    """
    Main function to load transactions, identify recurring ones, and log the result.

    Used only for testing purposes.

    """
    transactions = load_transactions_from_file(file_path)
    if not transactions:
        logging.error("No transactions found or failed to load transactions.")
        return

    recurring = identify_recurring_transactions(transactions)
    logging.info(f"Recurring Transactions: {recurring}")


if __name__ == "__main__":
    main('example.json')
