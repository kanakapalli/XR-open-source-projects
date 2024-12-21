import pandas as pd

# Load the uploaded CSV file
file_path = '../combined_try_it_out_links.csv'  # Update the path if needed
df = pd.read_csv(file_path)

# Rename the columns to match the desired names for consistency
df.rename(columns={
    'Project Name': 'project_name',
    'Short Description': 'short_description',
    'Project URL': 'project_url',
    'Try it Out Links': 'try_it_out_links'
}, inplace=True)

# Reorder columns as per the desired order
desired_order = ['project_name', 'try_it_out_links', 'short_description', 'project_url']
df = df[desired_order]

# Format links in markdown style
def format_multiple_links(links):
    """Convert multiple links separated by commas into Markdown format."""
    link_list = links.split(',')  # Split links by comma
    markdown_links = [f"[Link]({link.strip()})" for link in link_list]  # Format each link
    return ' '.join(markdown_links)  # Join with a space for Markdown formatting

df['try_it_out_links'] = df['try_it_out_links'].apply(format_multiple_links)
df['project_url'] = df['project_url'].apply(lambda x: f"[Link]({x})")

# Convert the updated DataFrame to a Markdown table
markdown_table = df.to_markdown(index=False)

# Save the Markdown table to a file
markdown_output_path = '../markdown_table_output.md'  # Output file path
with open(markdown_output_path, 'w') as f:
    f.write(markdown_table)

print(f"Markdown table saved to: {markdown_output_path}")
