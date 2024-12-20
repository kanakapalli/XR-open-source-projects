import pandas as pd

# Load the uploaded CSV file
file_path = 'combined_try_it_out_links.csv'
df = pd.read_csv(file_path)

# Convert the DataFrame to a Markdown table
markdown_table = df.to_markdown(index=False)

# Save the Markdown table to a file
markdown_output_path = 'markdown_table_output.md'
with open(markdown_output_path, 'w') as f:
    f.write(markdown_table)

markdown_output_path
