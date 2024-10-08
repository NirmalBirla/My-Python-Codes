from datetime import datetime, timedelta
import csv
import pandas as pd
import os

# Function for open file with given path
def open_file(path):
    with open(path, "r", encoding="utf-16") as file:
        lines = file.readlines()
    return lines

# Function to get first and last day of the month according to file name
def get_first_last_dates(file_name):
    # Split the input string into month and year
    month_name, year = file_name.split('_')
    year = int(year)
    
    # To get month nummber
    try:
        # Try full month name
        month_number = datetime.strptime(month_name.capitalize(), "%B").month
    except ValueError:
        # If it fails, try short month name
        month_number = datetime.strptime(month_name.upper(), "%b").month
    
    # Create the first date of the month
    first_date = datetime(year, month_number, 1)
    
    # Calculate the last date of the month
    if month_number == 12:
        last_date = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        last_date = datetime(year, month_number + 1, 1) - timedelta(days=1)
    
    return first_date.strftime("%Y-%m-%d"), last_date.strftime("%Y-%m-%d")

# Default directories to look for files
default_directory = "C:\\Users\\yunee\\OneDrive\\Desktop\\Salary_data\\"
downloads_directory = "C:\\Users\\yunee\\Downloads\\"

# An Example of filename 
print('\nFile name must like : Month followed by year (Example "JANUARY_2024" or "JAN_2024")')

# Ask user for the file name
filename = input("Enter your file name (with or without extension): ")

# Determine file extension and construct full paths
if "." not in filename:
    # If the filename doesn't include an extension, assume .txt
    file_path = os.path.join(default_directory, f"{filename}.txt")
    file_path_downloads = os.path.join(downloads_directory, f"{filename}.txt")
    filename += ".txt"
else:
    # If the filename includes an extension, use it as is
    file_path = os.path.join(default_directory, filename)
    file_path_downloads = os.path.join(downloads_directory, filename)

# Function to search for a file in a directory and its subdirectories
def search_file(directory, filename):
    for root, dirs, files in os.walk(directory):
        if filename in files:
            return os.path.join(root, filename)
    return None

# Attempt to open and read the file
try:
    # Try to open the file from the default directory
    if os.path.exists(file_path):
        lines = open_file(file_path)
            
    # If not found in the default directory, try the downloads folder
    elif os.path.exists(file_path_downloads):
        lines = open_file(file_path_downloads)

    # If not found in either directory, search the entire system
    else:
        print('\nFile not found in both Salary_data and Downloads folders. Searching the entire system...')
        file_location = search_file("C:\\", filename)  # Start searching from C:\
        if file_location:
            lines = open_file(file_location)
            
        else:
            print('\nFile not found in the entire system.')

    # Get user input for start_date and end_date
    file_name = filename.split('.')[0]
    start_date, end_date = get_first_last_dates(file_name)
    start_date = datetime.strptime(start_date, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
    print(f"\nProcessing from {start_date} to {end_date}")

    # It should be updated annually to reflect any changes or new holidays for the current year.
    # Make sure to review and modify this list at the start of each year to ensure accurate attendance management.

    holidays = ['2024-01-01','2024-01-26','2024-03-25','2024-08-15', '2024-08-19','2024-10-30','2024-10-31','2024-11-01'] # add holidays in this format "YYYY-MM-DD" (Example "2024-01-01")
    month_name = filename.split('_')[0]
    # To get month nummber
    try:
        # Try full month name
        month_number = datetime.strptime(month_name.capitalize(), "%B").month
    except ValueError:
        # If it fails, try short month name
        month_number = datetime.strptime(month_name.upper(), "%b").month
    month_holidays = []
    for date in holidays:
        if int(date[5:7]) == month_number:
            month_holidays.append(date)

    # Showing Holidays of this current month to the user 
    print(f"Holidays in this month : {month_holidays}\n")

    # Generate the list of weekdays
    date_list_ex_sat_sun = []
    current_date = start_date
    while current_date <= end_date:
        if current_date.weekday() < 5:  # 0 = Monday, 4 = Friday
            date_list_ex_sat_sun.append(current_date)
        current_date += timedelta(days=1)

    # Remove closed dates from the date_list
    date_list = [date for date in date_list_ex_sat_sun if str(date) not in holidays]

    # Create all required variables here
    employee_working_hours = {}
    employee_names = {}
    final = {}

    full_day_threshold = timedelta(hours=8, minutes=20)
    half_day_threshold = timedelta(hours=4)

    # Separate Important parts
    for line in lines[1:]:
        parts = line.split("\t")
        emp_id = parts[2]
        name = parts[3].title()
        date = datetime.strptime(parts[-1].strip(), "%Y-%m-%d %H:%M:%S").date()

        # Track employee names
        if emp_id not in employee_names:
            employee_names[emp_id] = name

        # Process only if date is in our list
        if date in date_list:
            if emp_id not in employee_working_hours:
                employee_working_hours[emp_id] = {}
            if date not in employee_working_hours[emp_id]:
                employee_working_hours[emp_id][date] = {"totalEntry": [], "name": name}
            time = datetime.strptime(parts[-1].strip(), "%Y-%m-%d %H:%M:%S").time()
            entry_key = f"{time.strftime('%H:%M:%S')}"
            employee_working_hours[emp_id][date]["totalEntry"].append(entry_key)

    # Create final dictionary ensuring all weekdays are included
    for emp_id in employee_names:
        for date in date_list:
            if date not in employee_working_hours.get(emp_id, {}):
                # Initialize absent day entry
                final.setdefault(emp_id, {})[date] = {
                    'name': employee_names[emp_id],
                    'duration': '00:00',
                    'total punch': [],
                    'punch': 'none',
                    'Status': 'A'
                }
            else:
                data = employee_working_hours[emp_id][date]
                length_of_totalEntry = len(data['totalEntry'])
                total_duration = timedelta()

                # Odd number of entries: skip the last entry for duration calculation
                if length_of_totalEntry % 2 != 0:
                    total_entries_for_duration = data['totalEntry'][:-1]
                    if len(total_entries_for_duration) > 1:
                        for i in range(0, len(total_entries_for_duration), 2):
                            odd_entry_time = datetime.strptime(total_entries_for_duration[i], "%H:%M:%S").time()
                            even_entry_time = datetime.strptime(total_entries_for_duration[i + 1], "%H:%M:%S").time()
                            odd_time = datetime.combine(datetime.today(), odd_entry_time)
                            even_time = datetime.combine(datetime.today(), even_entry_time)
                            time_difference = even_time - odd_time
                            total_duration += time_difference
                else:
                    odd_entry_time = []
                    even_entry_time = []
                    for i in range(0, length_of_totalEntry, 2):
                        odd_entry_time.append(datetime.strptime(data['totalEntry'][i], "%H:%M:%S").time())
                        even_entry_time.append(datetime.strptime(data['totalEntry'][i + 1], "%H:%M:%S").time())
                    for e, o in zip(even_entry_time, odd_entry_time):
                        even_time = datetime.combine(datetime.today(), e)
                        odd_time = datetime.combine(datetime.today(), o)
                        time_difference = even_time - odd_time
                        total_duration += time_difference

                # Calculating duration and attendance type
                total_seconds = total_duration.total_seconds()
                total_hours, remainder = divmod(total_seconds, 3600)
                total_minutes = remainder // 60
                duration_str = "{:02}:{:02}".format(int(total_hours), int(total_minutes))

                # Determine Full Day, Half Day, or Absent
                if total_duration >= full_day_threshold:
                    status = 'P'
                elif total_duration >= half_day_threshold:
                    status = 'HD'
                else:
                    status = 'A'

                # Adding data in the final dictionary
                final.setdefault(emp_id, {})[date] = {
                    'name': data['name'],
                    'Status': status,
                    'duration': duration_str,
                    'total punch': employee_working_hours[emp_id][date]["totalEntry"],
                    'punch': 'odd' if length_of_totalEntry % 2 != 0 else 'even',
                }

    # Export this data to CSV
    data_list = []
    for emp_id, dates in final.items():
        for date, data in dates.items():
            entry = {
                'Employee_ID': emp_id,
                'Name': data['name'],
                'Date': date.strftime('%Y-%m-%d'),  # Format date as YYYY-MM-DD
                'Status': data.get('Status'),
                'Duration': data['duration'],
                "Total_Punch": data['total punch'],
                'Punch_type': data['punch'],
            }
            data_list.append(entry)

    sorted_data_list = sorted(data_list, key=lambda x: (x['Employee_ID'], x['Date']))

    # Generating a CSV file
    csv_file_path = f'{file_name}_DAILY_REPORT.csv'
    with open(csv_file_path, 'w', newline='') as csv_file:
        fieldnames = ['Employee_ID', 'Date', 'Status', 'Duration', 'Name', 'Total_Punch', 'Punch_type']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for entry in sorted_data_list:
            writer.writerow(entry)
    print(f"CSV File generated as {csv_file_path}")

    # Generating an Excel file
    df = pd.DataFrame(data_list)
    excel_file_path = f'{file_name}_DAILY_REPORT.xlsx'
    df.to_excel(excel_file_path, index=False)
    print(f"Excel File generated as {excel_file_path}\n")


except FileNotFoundError:
    print('File not found in any of the directories or system.')
except UnicodeDecodeError:
    print('Error reading the file. It might not be encoded in UTF-16. Try a different encoding.')
except Exception as e:
    print(f"An error occurred: {e}")