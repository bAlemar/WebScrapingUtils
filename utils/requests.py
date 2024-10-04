import requests
import time

class Requests:
    
    def __init__(self) -> None:
        self.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        pass

    def get(self,url):
        response = requests.get(url,
                                headers=self.headers
                                )
        return response
    
    def get_with_cookies(self,url):
        response = requests.get(url)
        cookies = response.cookies
        response_final = requests.get(url,
                                      cookies=cookies,
                                      )
        return response_final

    def download_large_file_with_progress(self,url, destination_path):
        """
        Faz o download de um arquivo grande (ZIP) em blocos e exibe o progresso.

        Args:
            url (str): URL do arquivo para download.
            destination_path (str): Caminho onde o arquivo será salvo.
        """

        chunk_size = 1024
        downloaded_size = 0
        start_time = time.time()
        
        try:
            response = requests.get(url, headers=self.headers, stream=True, timeout=30)
            if response.status_code == 200:
                total_size = int(response.headers.get('Content-Length', 0))
                with open(destination_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size):
                        downloaded_size += len(chunk)
                        file.write(chunk)
                        self.__display_progress(downloaded_size, total_size, start_time)

                print(f"\nDownload concluído: {destination_path} ({total_size / (1024 * 1024):.2f} MB)")
            else:
                print(f"Erro ao baixar o arquivo: {response.status_code}")
        
        except requests.exceptions.Timeout:
            print("Erro: O tempo de conexão foi excedido (Timeout)")
        except requests.exceptions.RequestException as e:
            print(f"Erro: {e}")

    def __display_progress(self,downloaded_size, total_size, start_time):
        """
        Exibe o progresso do download, a velocidade e o tempo restante.

        Args:
            downloaded_size (int): Tamanho já baixado.
            total_size (int): Tamanho total do arquivo.
            start_time (float): Momento em que o download começou.
        """
        progress = downloaded_size / total_size * 100
        elapsed_time = time.time() - start_time
        download_speed = downloaded_size / elapsed_time
        remaining_time = (total_size - downloaded_size) / download_speed if download_speed > 0 else 0
        print(f"\rDownloaded: {progress:.2f}% | Speed: {download_speed / 1024:.2f} KB/s | Time left: {remaining_time:.2f} seconds", end='')


