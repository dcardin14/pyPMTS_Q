#12/26/2022 DC:  ChatGPT made this script for me.


import os
import csv

# Set the root directory you want to list
root_directory = 'O:\\FINANCE\\SS-CA\\Contracting\\PaymentRequests'

# Open the output CSV file for writing
with open('directory_listing.csv', 'w', newline='') as csvfile:
  # Create a CSV writer object
  writer = csv.writer(csvfile)
  # Write the column headers
  writer.writerow(['Name', 'Size', 'Modified Time', 'Path'])
  # Iterate over the directories and files in the root directory
  for root, dirs, files in os.walk(root_directory):
    # Skip the ARCHIVE subdirectory
    if 'ARCHIVE' in dirs:
      dirs.remove('ARCHIVE')
    # Iterate over the files in the current directory
    for filename in files:
      # Get the file's path
      file_path = os.path.join(root, filename)
      # Get the file's size and modified time
      file_size = os.stat(file_path).st_size
      file_modified_time = os.stat(file_path).st_mtime
      # Write the file's information to the CSV file
      writer.writerow([filename, file_size, file_modified_time, file_path])

