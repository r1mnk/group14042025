seconds = int(input(f"enter seconds: "))

seconds_in_minute = 60
seconds_in_hour = 60 * 60
seconds_in_day = 24 * 60 * 60
if 0 <= seconds <= 8640000:
    days = seconds // seconds_in_day
    hours = (seconds % seconds_in_day) // seconds_in_hour
    minutes = (seconds % seconds_in_hour) // seconds_in_minute
    remaining_seconds = seconds % seconds_in_minute

    if days == 1:
        day_str = "день"
    elif 2 <= days <= 4:
        day_str = "дні"
    else:
        day_str = "днів"

    formatted_time = f"{days} {day_str}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(remaining_seconds).zfill(2)}"

    print(formatted_time)
else:
    exit(1)
