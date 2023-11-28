import os
import pandas as pd
import json
from bs4 import BeautifulSoup

# Define the path to your folder
folder_path = '.\\your_folder_here\\'

# Initialize an empty list to hold the data
data = []

# Loop through every file in the directory
for filename in sorted(os.listdir(folder_path)):
    # Check if the filename points to a file
    if os.path.isfile(os.path.join(folder_path, filename)):
        # Open each file
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as f:
            contents = f.read()

            # Parse the HTML
            soup = BeautifulSoup(contents, 'html.parser')

            # Get the current page number
            current_page = int(soup.find('li', class_='current').get_text())

            # Find each item on the page
            items = soup.find_all('div', class_='mb-16 bg-white p-16 desktop:rounded-8 desktop:py-24 desktop:px-40')
            for i, item in enumerate(items, start=1):
                # Extract the data for each item
                thumbnail_link = item.find('img', class_='l-library-item-thumbnail')['src']
                item_url = item.find('a', target='_blank', rel='noopener')['href']
                item_name = item.find('div', class_='text-text-default font-bold typography-16 !preserve-half-leading mb-8 break-all').text
                author_name = item.find('div', class_='typography-14 text-text-gray600 !preserve-half-leading break-all').text
                author_url = item.find('a', target='_blank', class_='no-underline')['href']
                
                # Find each download block and extract the name and link
                download_blocks = item.find_all('div', class_='mt-16 desktop:flex desktop:justify-between desktop:items-center')
                files = [{'name': block.find('div', class_='typography-14 !preserve-half-leading').text, 'link': block.find('a', class_='no-underline flex items-center flex gap-4')['href']} for block in download_blocks]

                # Add the data to the list
                data.append({
                    'Page': current_page,
                    'Item Order': i,
                    'Item Name': item_name,
                    'Author Name': author_name,
                    'Thumbnail Link': thumbnail_link,
                    'Item URL': item_url,
                    'Author URL': author_url,
                    'Files': files
                })

# Get the maximum page number
max_page = max(item['Page'] for item in data)

# Update the order of the items
for item in data:
    item['Order'] = (max_page - item['Page']) * len(items) + (10 - item['Item Order'])
    del item['Page']
    del item['Item Order']

# Convert the list to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv(folder_path.strip('.\\') + '.csv', index=False)

# Save the data to a JSON file
with open(folder_path.strip('.\\') + '.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
