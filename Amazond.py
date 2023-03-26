import csv

# Get user input to search for a partial string, number or floating point
search_string = input("Enter the partial string, number or floating point to search in the amazon.csv file: ")

# Open the amazon.csv file
with open('amazon.csv', 'r') as file:

    # Create a CSV reader object
    reader = csv.DictReader(file)

    # Loop through each row in the CSV file
    for row in reader:

        # Check if the search_string is in the row, ignoring case
        if search_string.lower() in ','.join([value.lower() for value in row.values()]):

            # If the search_string is found, print the selected keys
            print("Order Date: ", row["Order Date"])
            print("Order ID: ", row["Order ID"])
            print("Item Total: ", row["Item Total"])
            print("Title: ", row["Title"])
