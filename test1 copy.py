import csv
import geoip2.database

reader = geoip2.database.Reader('GeoLite2-Country.mmdb')

# Open the input and output CSV files
with open('ip_addresses.csv', 'r', newline='') as input_file, open('https://ipdata9228.file.core.windows.net/ipdataaz993f/site/wwwroot/ip_addresses.csv', 'w', newline='') as output_file:
    # Create CSV reader and writer objects
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    # Loop through each row in the input file
    for row in csv_reader:
        ip_address = row[0].split(':')[0]
        port = row[0].split(':')[1]
        timestamp = row[1]
        try:
            response = reader.country(ip_address)
            country = response.country.name
        except geoip2.errors.AddressNotFoundError:
            country = 'Unknown'
        csv_writer.writerow([f"{ip_address}:{port},{timestamp}", country])
