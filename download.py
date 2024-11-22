# ADD THIS TO THE SCRIPT YOU WANT IT TO DOWNLOAD A PACKAGE FROM

import requests

url = 'http://localhost:8000/y<ourfile>.zip'  # Replace '<yourfile>.zip' with the name of the acctual package name
output_file = 'file.zip'  # Change this to your desired output file name

response = requests.get(url)

if response.status_code == 200:
    with open(output_file, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded: {output_file}")
else:
    print(f"Failed to download file: {response.status_code}")
