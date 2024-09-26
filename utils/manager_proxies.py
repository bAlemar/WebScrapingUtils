import random
from .filemanager import FileManager

class ProxyManager:
    """
    Manages proxies, keeping active proxies in use and deactivating failed ones.
    """
    def __init__(self, proxy_file_path='Webshare 100 proxies.txt') -> None:
        self.filemanager = FileManager()
        self.proxy_file_path = proxy_file_path
        self.proxy_list = self._load_proxy_list()
        self.current_proxy = self._format_proxy_for_playwright(random.choice(self.proxy_list))

    def get_proxy(self):
        """Returns the current proxy formatted for Playwright."""
        return self._format_proxy_for_playwright(self.current_proxy)

    def generate_proxy(self):
        """Generates a new active proxy formatted for requests."""
        while True:
            proxy = random.choice(self.proxy_list)
            if self._is_proxy_active(proxy):
                self.current_proxy = proxy
                return self._format_proxy_for_requests(proxy)

    def mark_proxy_as_successful(self, proxy):
        """Marks the given proxy as successful."""
        pos = self._find_proxy_position('server', proxy['server'])
        if pos is not None:
            self.proxy_list[pos]['Status'] = 1

    def mark_proxy_as_failed(self, proxy):
        """Marks the given proxy as failed."""
        pos = self._find_proxy_position('server', proxy['server'])
        if pos is not None:
            self.proxy_list[pos]['Status'] = 0
            self.current_proxy['Status'] = 0

    def _load_proxy_list(self):
        """Loads the proxy list from the file."""
        proxies = self.filemanager.read_file(self.proxy_file_path).strip().split('\n')
        proxy_list = []
        for pos, proxy in enumerate(proxies):
            ip, port, username, password = proxy.split(':')
            proxy_dict = {
                'pos': pos,
                'server': f'http://{ip}:{port}',
                'ip': ip,
                'port': port,
                'username': username,
                'password': password
            }
            proxy_list.append(proxy_dict)
        return proxy_list

    def _is_proxy_active(self, proxy):
        """Checks if the proxy is active."""
        return proxy.get('Status', 1) != 0

    def _find_proxy_position(self, key, value):
        """Finds the position of a proxy in the list by key and value."""
        return next((pos for pos, item in enumerate(self.proxy_list) if item.get(key) == value), None)

    def _format_proxy_for_playwright(self, proxy):
        """Formats the proxy for Playwright."""
        return {
            'server': proxy['server'],
            'username': proxy['username'],
            'password': proxy['password']
        }

    def _format_proxy_for_requests(self, proxy):
        """Formats the proxy for requests."""
        ip = proxy['ip']
        port = proxy['port']
        username = proxy['username']
        password = proxy['password']
        proxy_url = f'http://{username}:{password}@{ip}:{port}'
        return {
            'http': proxy_url,
            'https': proxy_url
        }
