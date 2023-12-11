def get_sleep_hours(input_str):
    if input_str == "":
        return f"0 hour 0 minute"

    start_time, end_time = input_str.split("-")

    def convert_to_24_hour(time):
        hours, minutes = map(int, time[:-2].split(":"))
        period = time[-2:].lower()

        if period == "pm" and hours != 12:
            hours += 12
        elif period == "am" and hours == 12:
            hours = 0

        return hours, minutes

    start = convert_to_24_hour(start_time)
    end = convert_to_24_hour(end_time)

    hours_diff = end[0] - start[0]
    minutes_diff = end[1] - start[1]

    if minutes_diff < 0:
        minutes_diff += 60
        hours_diff -= 1

    if hours_diff < 0:
        hours_diff += 24

    return f"{hours_diff} hours {minutes_diff} minutes"

def convert_hours_to_minutes(time):
    total_minutes  = float(time) * 60

    return int(total_minutes)

def convert_time_to_words(time):
     # Convert hours to minutes
    total_minutes = convert_hours_to_minutes(time)

    # Calculate whole hours and remaining minutes
    whole_hours = total_minutes // 60
    remaining_minutes = total_minutes % 60

    # Build the formatted string
    result_string = f"{whole_hours} hour(s) and {remaining_minutes} minute(s)"

    return result_string