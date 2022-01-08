"""
time_management.py:
File that contains function that returns today's date.
"""

import datetime


def time_teller():
    """Funktion that returns the date in the correct form."""

    time = datetime.datetime.now()
    day = time.day
    month = time.month
    year = time.year
    return f"{day}.{month}.{year}"
