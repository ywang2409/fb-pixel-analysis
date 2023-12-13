import pandas as pd

column_names_static = ['URL', 'Static Result']
column_names_dynamic = ['URL', 'Dynamic Result']

# Read the CSV file
df_static = pd.read_csv('data/static_res_1k.csv', header=None, names=column_names_static)
df_dynamic = pd.read_csv('data/dynamic_res_1k.csv', header=None, names=column_names_dynamic)

df = pd.merge(df_static, df_dynamic, on='URL')
# df.head(10)

# Count the number of sites using Facebook Pixel
pixel_count = 0
scrapable_count = 0

for row in df.iterrows():
    if row[1]['Static Result'] == "Found" or row[1]['Dynamic Result'] == "Found":
        pixel_count += 1
    
    if row[1]['Static Result'] == "Error" and row[1]['Dynamic Result'] == "Error":
        continue
    else:
        scrapable_count += 1

percentage_sites_with_pixel = (pixel_count / scrapable_count) * 100

# Print the results
print(f"Number of sites using Facebook Pixel: {pixel_count}")
print(f"Percentage of sites using Facebook Pixel: {percentage_sites_with_pixel}%")