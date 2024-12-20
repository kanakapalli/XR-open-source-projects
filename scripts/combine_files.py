import os
import pandas as pd

def combine_try_it_out_links(input_folder, output_file):
    """
    Combines "Try it Out Links" from multiple CSV files in a folder into a single CSV file.

    Parameters:
        input_folder (str): Path to the folder containing the CSV files.
        output_file (str): Path to save the combined CSV file.
    """
    # Initialize an empty list to store dataframes
    combined_data = []

    # Iterate through all files in the folder
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)

        # Check if the file is a CSV
        if file_name.endswith('.csv'):
            try:
                # Read the CSV file
                data = pd.read_csv(file_path)

                # Filter rows where "Try it Out Links" is not "No links available"
                filtered_data = data[data['Try it Out Links'] != "No links available"]

                # Append the filtered data to the list
                combined_data.append(filtered_data)
            except Exception as e:
                print(f"Error processing file {file_name}: {e}")

    # Combine all dataframes in the list
    if combined_data:
        result = pd.concat(combined_data, ignore_index=True)

        # Save the combined dataframe to the output file
        result.to_csv(output_file, index=False)
        print(f"Combined CSV file saved at: {output_file}")
    else:
        print("No valid data found in the folder.")

# Example usage
input_folder = "extrackedData"  # Replace with the path to your folder containing CSV files
output_file = "combined_try_it_out_links.csv"  # Replace with your desired output file path
combine_try_it_out_links(input_folder, output_file)
