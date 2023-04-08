import csv

# Read the input CSV file and extract the country names
with open('ip_addresses_with_country.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    countries = []
    visitors = []
    for row in reader:
        visitors.append(row[0])
        countries.append(row[1])
        

# Write the country names and visitors to a new CSV file with column headers
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Country', 'Visitors'])
    if len(countries) != len(visitors):
        print('Error: number of countries and visitors do not match')
    else:
        for i in range(len(countries)):
            writer.writerow([countries[i], visitors[i]])
