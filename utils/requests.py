import requests
import time
import logging
from typing import Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

class RequestHandler:
    
    def __init__(self) -> None:
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

    def get(self, url):
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response

    def get_with_cookies(self, url):
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()  # Raises HTTPError for bad responses
        cookies = response.cookies
        response_final = requests.get(url, cookies=cookies, headers=self.headers)
        response_final.raise_for_status()  # Raises HTTPError for bad responses
        return response_final

    def download_large_file_with_progress(self, url, destination_path):
        chunk_size = 1024
        downloaded_size = 0
        start_time = time.time()
        
        try:
            response = requests.get(url, headers=self.headers, stream=True, timeout=30)
            response.raise_for_status()  # Raises HTTPError for bad responses

            total_size = int(response.headers.get('Content-Length', 0))
            with open(destination_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size):
                    downloaded_size += len(chunk)
                    file.write(chunk)
                    self.__display_progress(downloaded_size, total_size, start_time)

            print(f"\nDownload completed: {destination_path} ({total_size / (1024 * 1024):.2f} MB)")
        except requests.exceptions.Timeout:
            print("Error: Connection timeout")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")

    def __display_progress(self, downloaded_size, total_size, start_time):
        progress = downloaded_size / total_size * 100
        elapsed_time = time.time() - start_time
        download_speed = downloaded_size / elapsed_time
        remaining_time = (total_size - downloaded_size) / download_speed if download_speed > 0 else 0
        time_left=f"Time left: {remaining_time:.2f} seconds"
        speed=f"Speed: {download_speed / 1024:.2f} KB/s"
        mask=f"\rDownloaded: {progress:.2f}% | {speed} | {time_left}"
        print(mask, end='')
        