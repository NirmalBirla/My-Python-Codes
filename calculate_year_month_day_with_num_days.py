num_days = int(input("Enter total days : "))
def calculate_y_m_d(num_days):
    years = 0
    months = 0
    days = 0
    if num_days > 365:
        years, num_days = divmod(num_days, 365)
    if num_days > 30:
        months, num_days = divmod(num_days, 30)
    if num_days < 30:
        days = num_days
    return years, months, days

years, months, days = calculate_y_m_d(num_days)
print(f"Year : {years} \nMonth : {months} \nDay : {days}")