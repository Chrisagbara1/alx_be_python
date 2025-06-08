from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("\nCurrent date and time:", formatted_current_date, "\n")
    return current_date  # Return the actual datetime object

def calculate_future_date():
    while True:
        current_date = display_current_datetime()
        
        print("(Enter 0 to exit)")
        try:
            add_days = int(input("Enter the number of days to add to the current date: "))
            if add_days == 0:
                print("Exiting program.")
                break

            # Add days using timedelta
            future_date = current_date + timedelta(days=add_days)
            formatted_future = future_date.strftime("%Y-%m-%d")
            print("Future date:", formatted_future)
        except ValueError:
            print("Please enter a valid number.")

calculate_future_date()