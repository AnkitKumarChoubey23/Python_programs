import pandas as pd

# Specify the path to your Excel file
file_path = 'path_to_your_file.xlsx'

# Read the Excel file into a pandas DataFrame
try:
    df = pd.read_excel(file_path)

    # Assuming the Excel file has columns named 'Name' and 'Money'
    if 'Name' in df.columns and 'Money' in df.columns:
        # Iterate through the rows to print name and associated money
        for index, row in df.iterrows():
            print(f"Name: {row['Name']}, Money: {row['Money']}")
    else:
        print("The file does not have 'Name' or 'Money' columns.")
except Exception as e:
    print(f"Error reading the Excel file: {e}")

    import pandas as pd

# Specify the path to your Excel file
file_path = 'path_to_your_file.xlsx'

# Read the Excel file into a pandas DataFrame
try:
    df = pd.read_excel(file_path)

    # Assuming the Excel file has columns named 'Name' and 'Money'
    if 'Name' in df.columns and 'Money' in df.columns:
        # Iterate through the rows and print name with associated money
        print("Printing data from Excel file:")
        for index, row in df.iterrows():
            print(f"Name: {row['Name']}, Money: {row['Money']}")
    else:
        print("The file does not have 'Name' or 'Money' columns.")
except Exception as e:
    print(f"Error reading the Excel file: {e}")