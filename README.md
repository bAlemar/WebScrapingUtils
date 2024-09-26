
# WebScrapingUtils

Este repositório contém utilitários para Web Scraping, incluindo uma ferramenta de gerenciamento de proxies que evita bloqueios durante automações de requisições. O código foi desenvolvido para facilitar a troca e o monitoramento de proxies de forma eficiente, permitindo a rotação automática para minimizar o risco de ser bloqueado por sites.

## Estrutura do Projeto

```bash
.
├── README.md            
└── utils
    ├── filemanager.py   
    ├── interfaces
    │   ├── manager_proxies.py  
    │   └── proxies.txt           
    └── manager_proxies.py 
```

### Explicação dos Arquivos
- **README.md**: Este arquivo, contendo a documentação do projeto.
- **utils/filemanager.py**: Gerencia a leitura e escrita de arquivos, como o `proxies.txt`, que armazena as proxies a serem testadas.
- **utils/interfaces/manager_proxies.py**: Interface para manipulação e gerenciamento das proxies.
- **utils/interfaces/proxies.txt**: Exemplo de arquivo contendo proxies a serem testadas e classificadas.
- **utils/manager_proxies.py**: Script principal que implementa o sistema de gestão de proxies, testando automaticamente sua disponibilidade e marcando-as conforme seu status.

## Como Usar

### Gerenciamento de Proxies
O principal objetivo deste projeto é evitar bloqueios ao realizar scraping em massa, rotacionando proxies automaticamente. O script em `manager_proxies.py` faz a gestão das proxies contidas no arquivo `proxies.txt`, testando sua funcionalidade e marcando as que estão boas ou bloqueadas.

### Exemplo de Uso
1. Adicione suas proxies no arquivo `proxies.txt` no formato `ip:port:username:password`.
2. Execute o script de gerenciamento para utilizar uma proxy válida e classificar sua performance.

```python
from utils.manager_proxies import ProxieManager

# Inicializando o gerenciador de proxies
proxie_manager = ProxieManager()

# Obtendo uma proxy funcional
proxy = proxie_manager.generate_proxy()

# Realizando requisições com a proxy
# Caso falhe, marque a proxy como falha
proxie_manager.mark_proxy_as_failed(proxy)
```

### Requisitos
- **Python 3.x**
- Dependências: certifique-se de instalar os pacotes necessários antes de rodar o projeto. Para isso, rode o seguinte comando:
```bash
pip install poetry
poetry install
```

## Contato

Se tiver dúvidas, sugestões ou quiser discutir o projeto, entre em contato!

- [Meu LinkedIn](https://www.linkedin.com/in/bernardo-alemar/)
- [GitHub](https://github.com/bAlemar)

Sinta-se à vontade para abrir uma issue ou enviar um PR com melhorias!

## Contribuindo

Pull requests são bem-vindos! Você pode contribuir com melhorias no código, novas funcionalidades ou ajustes na documentação. Para mudanças maiores, abra uma issue para discutirmos antes o que você gostaria de alterar.
