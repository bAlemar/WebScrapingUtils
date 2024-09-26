import random
import pytest
from unittest.mock import patch, MagicMock
from utils.manager_proxies import ProxyManager


@pytest.fixture
def proxy_manager():
    with patch(
        'utils.filemanager.FileManager.read_file', 
        return_value='127.0.0.1:8080:user:pass\n127.0.0.2:8080:user2:pass2'
    ):
        return ProxyManager()


def test_init(proxy_manager):
    assert len(proxy_manager.proxy_list) == 2
    assert proxy_manager.current_proxy is not None


def test_get_proxy(proxy_manager):
    result = proxy_manager.get_proxy()
    assert 'server' in result
    assert 'username' in result
    assert 'password' in result


def test_generate_proxy(proxy_manager):
    with patch('random.choice', side_effect=proxy_manager.proxy_list), patch.object(ProxyManager, '_is_proxy_active', return_value=True):
        proxy = proxy_manager.generate_proxy()
        assert proxy is not None
        assert 'http' in proxy
        assert 'https' in proxy


def test_mark_proxy_as_successful(proxy_manager):
    proxy = proxy_manager.proxy_list[0]
    proxy_manager.mark_proxy_as_successful(proxy)
    assert proxy['Status'] == 1


def test_mark_proxy_as_failed(proxy_manager):
    proxy = proxy_manager.proxy_list[0]
    proxy_manager.mark_proxy_as_failed(proxy)
    assert proxy['Status'] == 0
    assert proxy_manager.current_proxy['Status'] == 0


def test_is_proxy_active(proxy_manager):
    proxy = proxy_manager.proxy_list[0]
    proxy['Status'] = 1
    assert proxy_manager._is_proxy_active(proxy) is True
    proxy['Status'] = 0
    assert proxy_manager._is_proxy_active(proxy) is False


def test_format_proxy_for_playwright(proxy_manager):
    proxy = proxy_manager.proxy_list[0]
    result = proxy_manager._format_proxy_for_playwright(proxy)
    assert 'server' in result
    assert 'username' in result
    assert 'password' in result


def test_format_proxy_for_requests(proxy_manager):
    proxy = proxy_manager.proxy_list[0]
    result = proxy_manager._format_proxy_for_requests(proxy)
    assert 'http' in result
    assert 'https' in result


def test_find_proxy_position(proxy_manager):
    position = proxy_manager._find_proxy_position('server', 'http://127.0.0.1:8080')
    assert position == 0
    position = proxy_manager._find_proxy_position('server', 'non_existent')
    assert position is None
