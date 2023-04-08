import pandas as pd

# read the CSV file
df = pd.read_csv('country.csv')

# extract the first column containing the country names
countries = df.iloc[:, 0]

# create a dictionary to store the count of users for each country
user_count = {}

# loop through the remaining columns and update the count of users for each country
for column in df.iloc[:, 1:]:
    for i, user in enumerate(column):
        country = countries[i]
        if country not in user_count:
            user_count[country] = user
        else:
            user_count[country] += user

# sort the dictionary in descending order based on the count of users
sorted_user_count = dict(sorted(user_count.items(), key=lambda item: item[1], reverse=True))

# display the top N countries with the highest number of users
N = 5
print(f"Top {N} countries with the highest number of users:")
for i, (country, count) in enumerate(sorted_user_count.items()):
    if i == N:
        break
    print(f"{i+1}. {country}: {count} users")

# determine the country with the highest number of users and suggest a server
highest_user_country = max(user_count, key=user_count.get)
print(f"The country with the highest number of users is {highest_user_country}")
print("We recommend setting up a server in this country.")
