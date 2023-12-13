import pandas as pd
import matplotlib.pyplot as plt

column_names_static = ['URL', 'Static Result']
column_names_dynamic = ['URL', 'Dynamic Result']

# Read the CSV file
df_static = pd.read_csv('data/static_res_1k.csv', header=None, names=column_names_static)
df_dynamic = pd.read_csv('data/dynamic_res_1k.csv', header=None, names=column_names_dynamic)

df = pd.merge(df_static, df_dynamic, on='URL')

# Count the number of sites using Facebook Pixel
pixel_count = 0
scrapable_count = 0
static_count = 0
dynamic_count = 0
both_count = 0

for row in df.iterrows():
    if row[1]['Static Result'] == "Found" or row[1]['Dynamic Result'] == "Found":
        pixel_count += 1

        if row[1]['Static Result'] == "Found":
            static_count += 1
        if row[1]['Dynamic Result'] == "Found":
            dynamic_count += 1
    
    if row[1]['Static Result'] == "Found" and row[1]['Dynamic Result'] == "Found":
        both_count += 1

    if row[1]['Static Result'] == "Error" and row[1]['Dynamic Result'] == "Error":
        continue
    else:
        scrapable_count += 1


percentage_sites_with_pixel = (pixel_count / scrapable_count) * 100

# Create a pie chart
labels = ['Sites with Pixel', 'Sites without Pixel']
sizes = [pixel_count, scrapable_count - pixel_count]
colors = ['#ff9999', '#66b3ff']
explode = (0.1, 0)  # explode the first slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title('Facebook Pixel Usage')

# Show the pie chart
plt.show()


# Define the data
categories = ['Static', 'Dynamic', 'Both']
counts = [static_count, dynamic_count, both_count]

# Create the bar plot
plt.bar(categories, counts)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Counts')
plt.title('Websites Found using FB Pixel w. Different Methods')

# Add count numbers on the bars
for i, count in enumerate(counts):
    plt.text(i, count, str(count), ha='center', va='bottom')

# Show the bar plot
plt.show()

