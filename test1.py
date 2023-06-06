import pandas as pd

# Enter the roll number to search
roll_number = input("Enter the roll number: ")

# Read the Excel file
file_path = r'C:\Users\hplap\Downloads\FE All _ Compiled UT Marklist _ S1 _ AY  2022-23.xlsx'
df = pd.read_excel(file_path)

# Filter data for the entered roll number
student_data = df[df['ROLL NO.'] == roll_number]

# Check if student data is found
if not student_data.empty:
    # Display the result of the student
    print("Student Result:")
    print(student_data)

    # Find the highest and lowest results
    highest_result = df['Result'].max()
    lowest_result = df['Result'].min()

    # Display highest and lowest results
    print("\nHighest Result: ", highest_result)
    print("Lowest Result: ", lowest_result)
else:
    print("No data found for the entered roll number.")
