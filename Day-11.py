import datetime as date

def parse_date(date_str):
    # Convert input string to a datetime object, expecting format YYYY-MM-DD
    try:
        return date.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Oops! The date format should be YYYY-MM-DD. Please try again.")
        return None

# Ask the user to enter two dates
start_input = input("Enter the first date (YYYY-MM-DD): ")
end_input = input("Enter the second date (YYYY-MM-DD): ")

# Try converting inputs to datetime objects
start_date = parse_date(start_input)
end_date = parse_date(end_input)

# If both dates are valid, calculate and print the difference
if start_date and end_date:
    days_diff = abs((end_date - start_date).days)
    print(f"\nThere are {days_diff} days between {start_date.date()} and {end_date.date()}.")
