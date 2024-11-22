# ADD THIS TO THE SCRIPT YOU WANT IT TO DOWNLOAD A PACKAGE FROM

import requests
import zipfile
import os
import subprocess
import shutil

url = 'http://localhost:8000/<yourfile>.zip'  # Replace '<yourfile>.zip' with the actual package name
output_file = 'zip.zip'  # This is the name of the downloaded ZIP file. You can chage the name however you want
extracted_folder = ' '  # Folder to extract the contents to

response = requests.get(url)

if response.status_code == 200:
    with open(output_file, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded: {output_file}")

    with zipfile.ZipFile(output_file, 'r') as zip_ref:
        zip_ref.extractall(extracted_folder)
    print(f"Extracted contents to: {extracted_folder}")

    executable_file = os.path.join(extracted_folder, 'package.exe')  # Replace with the actual executable file name

    try:
        subprocess.run([executable_file], check=True)
        print(f"Executed: {executable_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing file: {e}")

    os.remove(output_file)
    print(f"Deleted ZIP file: {output_file}")
    shutil.rmtree(extracted_folder)
    print(f"Deleted extracted folder: {extracted_folder}")

else:
    print(f"Failed to download file: {response.status_code}")
