# last day of month

from datetime import timedelta

def get_is_end_of_month(date):
    tomorrow = date.date() + timedelta(days=1)
    
    if tomorrow.day == 1:
        return 1
    
    return 0



lastday_of_months_list = []
for date in df.index:
    lastday_of_months_list.append(get_is_end_of_month(date))
