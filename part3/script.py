import csv
import matplotlib.pyplot as plt
from datetime import datetime

# Initialize lists to store dates and values
dates = []
values = []

# Read data from the CSV file
with open('accesses.csv', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        # Split the row into value and date
        value = int(row[0])
        date_str = row[1]
        # Convert date string to datetime object
        date = datetime.strptime(date_str, '%d/%b/%Y')
        # Append to the lists
        values.append(value)
        dates.append(date)

# Plotting the data
plt.figure(figsize=(10, 6))
plt.bar(dates, values, color='skyblue')
plt.title('Accesses Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Accesses')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('accesses.pdf')
# Show the plot

