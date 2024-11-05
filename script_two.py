# Import all the requirements
from datetime import timedelta, datetime
import pandas as pd
import csv
import io

# Initialize variables to store the data 
attendance_data = {}
final_data = []

# An Example of filename 
print('\nFile name must like : Month followed by year (Example "JANUARY_2024")')

# Ask user for the file name
filename = input("Enter your file name (with or without extension): ")

# Determine file extension and construct full paths
if "." in filename:
    file_name = filename.split('.')[0]
else:
    file_name = filename

# Open the CSV file and process it
path = fr"C:\Users\yunee\OneDrive\Desktop\Salary_data\{file_name}_DAILY_REPORT.csv" # Change paths according to your system.

try:
    with open(path, mode='r', encoding='ISO-8859-1', errors='ignore') as file:
        csv_reader = csv.reader(x.replace('\x00', '') for x in file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            if len(row) < 4:  # Check if the row has at least 4 columns
                continue  # Skip this row if it doesn't have enough columns
            emp_id = row[0]
            status = row[2]
            duration_str = row[3]
            name = row[4]
            # print(f"Processing: emp_id={emp_id}, name={name}, duration={duration_str}")
            # Convert duration to timedelta
            hours, minutes = map(int, duration_str.split(':'))
            duration = timedelta(hours=hours, minutes=minutes)
            if emp_id not in attendance_data:
                attendance_data[emp_id] = {
                    'name': name,
                    'total_duration': timedelta(),
                    'total_full_days' : 0,
                    'total_half_days' : 0,
                    'total_absent' : 0,
                    'total_work_days' : 0,
                    'total_month_working_days' : 0
                }
            # Update total duration
            attendance_data[emp_id]['total_duration'] += duration

            # Counting full day, half day, or absent
            if status == 'P':
                attendance_data[emp_id]['total_full_days'] += 1
                attendance_data[emp_id]['total_work_days'] += 1
            elif status == 'HD':
                attendance_data[emp_id]['total_half_days'] += 1
                attendance_data[emp_id]['total_work_days'] += 0.5
            else:
                attendance_data[emp_id]['total_absent'] += 1

            attendance_data[emp_id]['total_month_working_days'] += 1

    # Add header row
    final_data.append([
        "S.No.",
        "ID",
        "Name",
        "Total Work Hours",
        "Full Days",
        "Half Days",
        "Absent",
        "Total Working Days(FD+HD)",
        "Total Month Working Days"
    ])
    sr_no = 1
    for emp_id, data in attendance_data.items():
        total_duration = data['total_duration']
        total_hours = f"{int(total_duration.total_seconds() // 3600)}:{(int(total_duration.seconds % 3600) // 60)}"
        final_data.append([
            sr_no,
            emp_id,
            data['name'],
            total_hours,
            data['total_full_days'],
            data['total_half_days'],
            data['total_absent'],
            data['total_work_days'],
            data['total_month_working_days']
        ])
        sr_no += 1
    # Define the output file path
    current_month_year = datetime.now().strftime("%B_%Y")
    output_path = f"{file_name}_MONTHLY_REPORT.csv"

    # Generating a CSV file
    with open(output_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(final_data)
    print(f"\nCSV File generated as {output_path}")

    # Generating an Excel file
    df = pd.DataFrame(final_data)
    excel_file_path = f'{file_name}_MONTHLY_REPORT.xlsx'
    df.to_excel(excel_file_path, index=False)
    print(f"Excel File generated as {excel_file_path}\n")

except FileNotFoundError:
    print("You need to run the first_script.py file first.")
except UnicodeDecodeError:
    print('Error reading the file. It might not be encoded in UTF-16. Try a different encoding.')
except Exception as e:
    print(f"An error occurred: {e}")