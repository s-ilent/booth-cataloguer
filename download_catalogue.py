import os
import requests
from bs4 import BeautifulSoup
from http.cookiejar import MozillaCookieJar
from urllib.parse import urljoin

def load_cookies(file_path):
    cj = MozillaCookieJar()
    cj.load(file_path, ignore_discard=True, ignore_expires=True)
    return requests.utils.dict_from_cookiejar(cj)

def save_page(url, folder, page_num, cookies):
    response = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Save the page
    with open(os.path.join(folder, f'{page_num}.html'), 'w', encoding='utf-8') as f_out:
        f_out.write(str(soup))
    
    # Download images
    img_folder = os.path.join(folder, f'{page_num}_files')
    os.makedirs(img_folder, exist_ok=True)
    for img in soup.find_all('img'):
        img_url = urljoin(url, img.get('src'))
        img_data = requests.get(img_url, cookies=cookies).content
        img_file = os.path.join(img_folder, os.path.basename(img_url))
        with open(img_file, 'wb') as f_out:
            f_out.write(img_data)

def main():
    base_url = 'https://accounts.booth.pm'
    first_page_url = base_url + '/library'
    target_dir = 'your_folder_here'  # Specify your target directory here
    
    # Load cookies from a Netscape HTTP Cookie File
    cookies = load_cookies('cookies.txt')
    
    # Save the first page
    save_page(first_page_url, target_dir, 1, cookies)
    
    # Parse the first page to find the total number of pages
    response = requests.get(first_page_url, cookies=cookies)
    soup = BeautifulSoup(response.text, 'html.parser')
    #last_page_num = int(soup.find('a', {'class': 'nav-item last-page'}).get('href').split('=')[-1])
    last_page_link = soup.find('a', {'class': 'nav-item last-page'})
    last_page_url = last_page_link.get('href')
    last_page_num = int(last_page_url.split('=')[-1])
    
    # Save the rest of the pages
    for page_num in range(2, last_page_num + 1):
        page_url = base_url + '/library?page=' + str(page_num)
        save_page(page_url, target_dir, page_num, cookies)

if __name__ == '__main__':
    main()
