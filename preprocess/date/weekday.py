week_days= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']

def getDayOfWeek(date):
    
    day=date.weekday()

    return week_days[day]
