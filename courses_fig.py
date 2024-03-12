import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import os
# Your DataFrame
data = {
    'Year': [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Teaching Hours': [64, 64, 64, 150, 0, 0, 150, 150, 200, 194, 194, 194, 115, 169, 100, 169],
    'Event': ['', '', '', '', 'Postdoc', 'New position', '', '', '', '', '', '', 'Maternity Leave', '', 'Maternity Leave', '']
}


# Check the lengths of arrays
lengths = {key: len(arr) for key, arr in data.items()}

# Verify that all lengths are the same
if len(set(lengths.values())) > 1:
    print("Lengths of arrays:")
    for key, length in lengths.items():
        print(f"{key}: {length}")
    raise ValueError("All arrays must be of the same length")

# Create DataFrame
df = pd.DataFrame(data)

# Fill missing values in 'Event' with a default value
default_event = 'No Event'  # You can change this to any default value you prefer
df['Event'] = df['Event'].replace('', default_event)
# Replace years in the 'Year' column
df['Year'] = df['Year'].astype(str) + '-' + (df['Year'] + 1).astype(str)

# Display the DataFrame
print(df)


# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
plt.bar(df['Year'], df['Teaching Hours'], color='cadetblue')

# Adding event markers
for index, row in df.iterrows():
    if row['Event'] == 'Maternity Leave':
        plt.text(row['Year'], row['Teaching Hours'] + 10, 'Maternity Leave', ha='center', va='bottom', rotation=90)
    if row['Event'] == 'Postdoc':
        plt.text(row['Year'], row['Teaching Hours'] + 10, 'Postdoc', ha='center', va='bottom', rotation=90)
    if row['Event'] == 'New position':
        plt.text(row['Year'], row['Teaching Hours'] + 10, 'New position', ha='center', va='bottom', rotation=90)
# Update x-axis labels with the 'Year' column
plt.xticks(range(len(df)), df['Year'], rotation=90, ha='center')  # Setting rotation to 0 and ha to 'center'

plt.xlabel('Year', rotation=0, ha='center')  # Setting rotation to 0 and ha to 'center'
plt.ylabel('Teaching Hours without the coordination time')
# Adjust space at the top and bottom
plt.subplots_adjust(top=0.99, bottom=0.2,right=0.99,left=0.08)
# Save the figure as a PNG file

# Specify the directory to save the image
img_directory = 'img'
os.makedirs(img_directory, exist_ok=True)

plt.savefig(os.path.join(img_directory, 'teaching_hours_figure.png'))

plt.show()
