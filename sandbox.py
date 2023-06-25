from datetime import datetime, timedelta


def current_week():
    start_date = datetime.now()
    end_date = start_date + timedelta(days=7)
    items = [start_date]
    week_str = []

    while start_date < end_date:
        start_date += timedelta(days=1)
        items.append(start_date)

    for date in items:
        week_str.append(date.strftime("%B %d, %A"))

    return week_str


print(current_week())
