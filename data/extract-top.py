import pandas as pd

def extract_top_lines(input_file, output_file, num_lines):
    # Read the input CSV file
    df = pd.read_csv(input_file)

    # Extract the top 'num_lines' lines
    top_lines = df.head(num_lines)

    # Write the top lines to a new CSV file
    top_lines.to_csv(output_file, index=False)

input_file = 'tranco_3V2KL.csv'
output_file = 'top_1k.csv'
num_lines = 1000

extract_top_lines(input_file, output_file, num_lines)