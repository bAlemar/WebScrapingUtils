import os
import csv 
import json
from typing import Any,Dict,List


class FileManager:

    def __init__(self) -> None:
        pass
    
    def open_json(self,path:str):
        with open(path, 'r') as file:
            dados = json.load(file)
        return dados

    def save_pdf(self,path:str,file_name:str,pdf) -> None:    
        self.check_path(path)
        path_pdf = rf'{path}/{file_name}.pdf'
        with open(path_pdf, 'wb') as file_path:
            file_path.write(pdf)
        

    def save_json(self,path:str,file_name:str,json_data) -> None:
        self.check_path(path)
        path_json = rf'{path}/{file_name}.json'
        with open(path_json, 'w') as json_file:
            json.dump(json_data, json_file, indent=4)

    def save_soup(self,path:str,file_name:str,soup) -> None:
        self.check_path(path)
        path_soup = rf'{path}/{file_name}.html'
        with open(path_soup,'w',encoding='utf-8') as file:
            file.write(soup.prettify())
    
    def check_path(self,file_path:str) -> None:
        if not os.path.exists(file_path):
            os.makedirs(file_path)

    def check_file_exists(self,file) -> bool:
        if os.path.isfile(file):
            return True
        else: 
            return False

    def open_html(self,path):
        with open(path, 'r', encoding='utf-8') as arquivo:
            html = arquivo.read()
        return html
    
    def get_all_html_from_path(self,path) -> Dict:
        """
        Dicionario com html e nome arquivo
        """
        lista_files = {}
        for arquivo in os.listdir(path):
            html = self.get_html_from_path(rf'{path}/{arquivo}')
            lista_files[arquivo[:-5]] = html
        return lista_files
    
    def read_file(self,path):
         with open(path, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            return conteudo
         
    def create_and_write_csv(self,path,file_name,columns,data):
        self.create_csv(path,file_name,columns)
        self.write_to_csv(path,file_name,columns,data)
        return
    
    def create_csv(self,path:str,file_name:str, columns: List):
        file_path = rf'{path}/{file_name}.csv'
        # Cria o arquivo CSV e escreve o cabeçalho com as colunas
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(columns)
    
    def write_to_csv(self,path:str,file_name:str,data:List):
        file_path = rf'{path}/{file_name}.csv'
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data)
    
    def save_file(self,path,file):
        with open(path, 'wb') as file_path:
            file_path.write(file)
    
    def get_proxie_list(self):
        path_proxie_txt = r'proxies.txt'
        proxies = self.read_file(path_proxie_txt)
        return proxies.strip().split('\n')

    def get_files_from_path(self,path,endwith=None):
        return [x for x in os.listdir(path) if x.endswith(endwith)] 

