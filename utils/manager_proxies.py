from filemanager import FileManager
import random

class ProxieManager:
    """
    Manter sempre a proxie que está funcionando ativa, caso pare de funcionar vai para zona proxy inativa
    """
    def __init__(self) -> None:
        self.filemanager = FileManager()
        self.lista_proxies = self.__get_proxie_list()
        self.proxie = self.__format_proxy_to_playwright(random.choice(self.lista_proxies))
        self.path_proxie_txt = r'Webshare 100 proxies.txt' # INSIRA SEU TXT COM PROXIE AQ
    
    def get_proxy(self):
        return self.__format_proxy_to_playwright(self.proxie)

    def generate_proxy(self):
        """
        Take new Proxie that is Status 1 or doesn't get test
        """      
        while True:
            proxie = random.choice(self.lista_proxies)
            if self.__check_status_proxy(proxie):
                self.proxie = proxie 
                return self.__format_proxy_to_requests(proxie)
        
    def mark_proxy_as_sucessful(self,proxy):
        chave = 'server'
        valor = proxy['server']
        pos = self.__find_pos_proxy(chave,valor)
        self.lista_proxies[pos].update({'Status':1})

    def mark_proxy_as_failed(self,proxy):
        chave = 'server'
        valor = proxy['server']
        pos = self.__find_pos_proxy(chave,valor)
        self.lista_proxies[pos].update({'Status':0})
        self.proxie.update({'Status':0})
    
    
    def __get_proxie_list(self):
        proxies = self.filemanager.read_file(self.path_proxie_txt)
        lista_proxies = proxies.strip().split('\n')
        lista_final_proxy = []
        for pos,proxie in enumerate(lista_proxies):
            proxie = proxie.split(':')
            ip = proxie[0]
            port = proxie[1]
            username = proxie[2]
            password = proxie[3]
            dict_proxie = {'pos':pos,
                            'server':f'http://{ip}:{port}',
                            'ip':ip,
                            'port':port,
                            'username':username,
                            'password':password}
            lista_final_proxy.append(dict_proxie)

        self.lista_proxies = lista_final_proxy
        return lista_final_proxy

    def __check_status_proxy(self,proxy):
        # Casos: Com Status(1 ou 0) e Sem Status
        if 'Status' in proxy.keys():
            if proxy['Status'] == 0:
                return False
        else:
            return True
    
    def __find_pos_proxy(self,chave,valor):
        return next((pos for pos,item in enumerate(self.lista_proxies) if item.get(chave) == valor), None)

    def __format_proxy_to_playwright(self,proxy):
        return {
            'server': proxy['server'],
            'username':proxy['username'],
            'password':proxy['password']
        }
    
    def __format_proxy_to_requests(self,proxy):
        ip = proxy['ip']
        porta = proxy['port']
        username = proxy['username']
        password = proxy['password']
        return{
            'http':rf'http://{username}:{password}@{ip}:{porta}',
            'https':rf'http://{username}:{password}@{ip}:{porta}'
        }