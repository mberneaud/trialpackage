# This is a trial package code
from datetime import date

def try_me(name="stranger"):
    """
    Prints the current date and the name of the user passed via CLI. If no argument
    is passed, user will be called "stranger"
    """
    today = date.today()
    print(f"Today is {today}. Have a wonderful day, {name}!")
    if name=="stranger":
        print("Hint: Try calling me with your name passed as the first argument")


if __name__ == "__main__":
    try_me()
