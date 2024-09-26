import os
import csv
import json
from typing import Any, Dict, List, Optional
from bs4 import BeautifulSoup  # Assuming BeautifulSoup is used for 'soup' objects


class FileManager:
    """
    A utility class for managing file operations such as reading, writing, and ensuring directory existence.
    """

    def open_json(self, path: str) -> Any:
        """
        Opens a JSON file and returns its content.

        Args:
            path (str): The path to the JSON file.

        Returns:
            Any: The content of the JSON file.
        """
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def save_pdf(self, path: str, file_name: str, pdf: bytes) -> None:
        """
        Saves a PDF file to the specified path.

        Args:
            path (str): The directory path where the PDF will be saved.
            file_name (str): The name of the PDF file.
            pdf (bytes): The PDF content in bytes.
        """
        self._ensure_directory_exists(path)
        path_pdf = os.path.join(path, f'{file_name}.pdf')
        with open(path_pdf, 'wb') as file:
            file.write(pdf)

    def save_json(self, path: str, file_name: str, json_data: Any) -> None:
        """
        Saves JSON data to a file.

        Args:
            path (str): The directory path where the JSON file will be saved.
            file_name (str): The name of the JSON file.
            json_data (Any): The JSON data to be saved.
        """
        self._ensure_directory_exists(path)
        path_json = os.path.join(path, f'{file_name}.json')
        with open(path_json, 'w', encoding='utf-8') as json_file:
            json.dump(json_data, json_file, indent=4)

    def save_soup(self, path: str, file_name: str, soup: BeautifulSoup) -> None:
        """
        Saves BeautifulSoup object as an HTML file.

        Args:
            path (str): The directory path where the HTML file will be saved.
            file_name (str): The name of the HTML file.
            soup (BeautifulSoup): The BeautifulSoup object to be saved.
        """
        self._ensure_directory_exists(path)
        path_soup = os.path.join(path, f'{file_name}.html')
        with open(path_soup, 'w', encoding='utf-8') as file:
            file.write(soup.prettify())

    def _ensure_directory_exists(self, directory: str) -> None:
        """
        Ensures that the specified directory exists, creating it if necessary.

        Args:
            directory (str): The directory path to check or create.
        """
        os.makedirs(directory, exist_ok=True)

    def file_exists(self, file_path: str) -> bool:
        """
        Checks if a file exists at the specified path.

        Args:
            file_path (str): The path to the file.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        return os.path.isfile(file_path)

    def open_html(self, path: str) -> str:
        """
        Opens an HTML file and returns its content as a string.

        Args:
            path (str): The path to the HTML file.

        Returns:
            str: The content of the HTML file.
        """
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()

    def get_all_html_from_path(self, path: str) -> Dict[str, str]:
        """
        Retrieves all HTML files from a directory and returns their content.

        Args:
            path (str): The directory path to search for HTML files.

        Returns:
            Dict[str, str]: A dictionary with file names (without extension) as keys and HTML content as values.
        """
        html_files = {}
        for file_name in os.listdir(path):
            if file_name.endswith('.html'):
                html = self.open_html(os.path.join(path, file_name))
                html_files[file_name[:-5]] = html
        return html_files

    def read_file(self, path: str) -> str:
        """
        Reads the content of a file and returns it as a string.

        Args:
            path (str): The path to the file.

        Returns:
            str: The content of the file.
        """
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()

    def create_and_write_csv(self, path: str, file_name: str, columns: List[str], data: List[List[Any]]) -> None:
        """
        Creates a CSV file and writes data to it.

        Args:
            path (str): The directory path where the CSV file will be saved.
            file_name (str): The name of the CSV file.
            columns (List[str]): The column headers for the CSV file.
            data (List[List[Any]]): The data to be written to the CSV file.
        """
        self.create_csv(path, file_name, columns)
        self.write_to_csv(path, file_name, data)

    def create_csv(self, path: str, file_name: str, columns: List[str]) -> None:
        """
        Creates a CSV file with the specified columns.

        Args:
            path (str): The directory path where the CSV file will be saved.
            file_name (str): The name of the CSV file.
            columns (List[str]): The column headers for the CSV file.
        """
        file_path = os.path.join(path, f'{file_name}.csv')
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(columns)

    def write_to_csv(self, path: str, file_name: str, data: List[List[Any]]) -> None:
        """
        Writes data to an existing CSV file.

        Args:
            path (str): The directory path where the CSV file is located.
            file_name (str): The name of the CSV file.
            data (List[List[Any]]): The data to be written to the CSV file.
        """
        file_path = os.path.join(path, f'{file_name}.csv')
        with open(file_path, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(data)

    def save_file(self, path: str, file_content: bytes) -> None:
        """
        Saves binary content to a file.

        Args:
            path (str): The path where the file will be saved.
            file_content (bytes): The binary content to be saved.
        """
        with open(path, 'wb') as file:
            file.write(file_content)

    def get_proxies_list(self) -> List[str]:
        """
        Retrieves a list of proxies from a file named 'proxies.txt'.

        Returns:
            List[str]: A list of proxies.
        """
        path_proxies_txt = 'proxies.txt'
        proxies = self.read_file(path_proxies_txt)
        return proxies.strip().split('\n')

    def get_files_from_path(self, path: str, endwith: Optional[str] = None) -> List[str]:
        """
        Retrieves a list of files from a directory, optionally filtering by file extension.

        Args:
            path (str): The directory path to search for files.
            endwith (Optional[str]): The file extension to filter by (e.g., '.txt').

        Returns:
            List[str]: A list of file names.
        """
        return [file for file in os.listdir(path) if endwith is None or file.endswith(endwith)]
