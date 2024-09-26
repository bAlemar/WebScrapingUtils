import os
import json
import pytest
import csv
from unittest.mock import patch, mock_open, MagicMock
from utils.filemanager import FileManager
from bs4 import BeautifulSoup

@pytest.fixture
def file_manager():
    return FileManager()

def test_save_json(file_manager):
    json_data = {'key': 'value'}
    expected_json_output = json.dumps(json_data, indent=4)  # Assuming indent=4 based on the multiple calls

    with patch('os.makedirs') as mock_makedirs, patch('builtins.open', mock_open()) as mock_file:
        file_manager.save_json('fake_path', 'test_json', json_data)
        mock_makedirs.assert_called_once_with('fake_path', exist_ok=True)
        
        # Retrieve the file handle from the mock
        handle = mock_file()

        # Combine the write calls into a single string and compare with expected output
        written_data = ''.join(call.args[0] for call in handle.write.mock_calls)
        assert written_data == expected_json_output

def test_save_pdf(file_manager):
    pdf_content = b'%PDF-1.4'
    with patch('os.makedirs') as mock_makedirs, patch('builtins.open', mock_open()) as mock_file:
        file_manager.save_pdf('fake_path', 'test_pdf', pdf_content)
        mock_makedirs.assert_called_once_with('fake_path', exist_ok=True)
        mock_file().write.assert_called_once_with(pdf_content)


def test_save_soup(file_manager):
    soup = BeautifulSoup('<html></html>', 'html.parser')
    with patch('os.makedirs') as mock_makedirs, patch('builtins.open', mock_open()) as mock_file:
        file_manager.save_soup('fake_path', 'test_soup', soup)
        mock_makedirs.assert_called_once_with('fake_path', exist_ok=True)
        mock_file().write.assert_called_once_with(soup.prettify())

def test_file_exists(file_manager):
    with patch('os.path.isfile', return_value=True) as mock_isfile:
        assert file_manager.file_exists('fake_file')
        mock_isfile.assert_called_once_with('fake_file')

def test_open_html(file_manager):
    html_content = '<html></html>'
    with patch('builtins.open', mock_open(read_data=html_content)):
        result = file_manager.open_html('fake_path')
        assert result == html_content

def test_get_all_html_from_path(file_manager):
    html_content = '<html></html>'
    files = ['file1.html', 'file2.html']
    with patch('os.listdir', return_value=files), patch('utils.filemanager.FileManager.open_html', return_value=html_content):
        result = file_manager.get_all_html_from_path('fake_path')
        assert result == {'file1': html_content, 'file2': html_content}

def test_create_and_write_csv(file_manager):
    columns = ['col1', 'col2']
    data = [['data1', 'data2'], ['data3', 'data4']]
    with patch('builtins.open', mock_open()), patch('csv.writer') as mock_writer:
        writer_instance = mock_writer.return_value
        file_manager.create_and_write_csv('fake_path', 'test_csv', columns, data)
        writer_instance.writerow.assert_called_once_with(columns)
        writer_instance.writerows.assert_called_once_with(data)

def test_save_file(file_manager):
    file_content = b'binary data'
    with patch('builtins.open', mock_open()) as mock_file:
        file_manager.save_file('fake_path', file_content)
        mock_file().write.assert_called_once_with(file_content)

def test_get_proxies_list(file_manager):
    proxies_data = 'proxy1\nproxy2\nproxy3'
    with patch('utils.filemanager.FileManager.read_file', return_value=proxies_data):
        result = file_manager.get_proxies_list()
        assert result == ['proxy1', 'proxy2', 'proxy3']

def test_get_files_from_path(file_manager):
    files = ['file1.txt', 'file2.txt', 'file3.html']
    with patch('os.listdir', return_value=files):
        result = file_manager.get_files_from_path('fake_path', endwith='.txt')
        assert result == ['file1.txt', 'file2.txt']
