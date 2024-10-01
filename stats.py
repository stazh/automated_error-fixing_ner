# Create stats

import os
import csv

output_csv = 'statistics.csv'  # Output CSV file for the statistics

# Use a dictionary to hold statistics for each file
statistics = {}

def write_to_statistics(file, stats_name, stats_value):
    """Adds statistics to the dictionary.
    
    Args:
        file (str): The filename that the statistics relate to.
        stats_name (str): The name of the statistic (e.g., 'Number of Entities Before Processing').
        stats_value (int): The value of the statistic.
    """
    
    # If the file is not in the statistics dictionary, add it
    if file not in statistics:
        statistics[file] = {}  # Initialize an empty dictionary for this file

    # Update the statistic for the corresponding filename
    statistics[file][stats_name] = stats_value

def save_statistics_to_csv():
    """Writes all collected statistics to the CSV file at once."""
    
    file_exists = os.path.isfile(output_csv)

    # Prepare fieldnames for the CSV, starting with 'Filename'
    fieldnames = ['Filename'] + list(set(key for stats in statistics.values() for key in stats.keys()))

    with open(output_csv, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()  # Write header

        # Write each filename's statistics to the CSV
        for file, stats in statistics.items():
            # Create a row with 'Filename' and corresponding stats
            row = {'Filename': file}
            row.update(stats)  # Merge stats into the row dictionary
            writer.writerow(row)

    print(f"Statistics saved to {output_csv}")

# Example of how to use the function
# write_to_statistics('example.xml', 'Number of Entities After Processing', 5)
# write_to_statistics('example.xml', 'Number of Entities Before Processing', 10)
# save_statistics_to_csv()
