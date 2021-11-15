# This is a trial package code
from datetime import date
import sys

def try_me():
    if len(sys.argv) == 1:
        name = "stranger"
    else:
        name = sys.argv[1]
    today = date.today()
    print(f"Today is {today}. Have a wonderful day, {name}!")


if __name__ == "__main__":
    try_me()
