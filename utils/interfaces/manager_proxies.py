from abc import ABC, abstractmethod

class ProxieManagerInterface(ABC):
    """
    Interface para gerenciar proxies
    """
    
    @abstractmethod
    def get_proxy(self):
        """
        Retorna o proxy atual no formato Playwright
        """
        pass
    
    @abstractmethod
    def generate_proxy(self):
        """
        Gera um novo proxy que está com Status 1 ou ainda não foi testado.
        Retorna o proxy no formato apropriado para Requests
        """
        pass

    @abstractmethod
    def mark_proxy_as_sucessful(self, proxy):
        """
        Marca o proxy como bem-sucedido (Status 1)
        """
        pass

    @abstractmethod
    def mark_proxy_as_failed(self, proxy):
        """
        Marca o proxy como falho (Status 0)
        """
        pass
