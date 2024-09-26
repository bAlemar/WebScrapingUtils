# WebScrapingUtils

Este repositório contém utilitários para Web Scraping, incluindo uma ferramenta simples de gerenciamento de proxies que evita bloqueios em sites durante a automação de requisições. O código foi desenvolvido para facilitar a troca e o monitoramento de proxies de forma eficiente.

## Estrutura do Projeto

```bash
.
├── README.md            
└── utils
    ├── filemanager.py   
    ├── interfaces
    │   ├── manager_proxies.py  
    │   └── proxie.txt           
    └── manager_proxies.py 
```

### Explicação dos Arquivos
- **README.md**: Este arquivo, contendo a documentação do projeto.
- **utils/filemanager.py**: Gerencia a leitura e escrita de arquivos de proxies, como `proxie.txt`.
- **utils/interfaces/manager_proxies.py**: Interface para manipulação de proxies.
- **utils/interfaces/proxie.txt**: Exemplo de arquivo contendo proxies para serem testadas e classificadas.
- **utils/manager_proxies.py**: Script principal que implementa o sistema de gestão de proxies, classificando e testando automaticamente as proxies com base em seu status.

## Como Usar

### Gerenciamento de Proxies
O principal objetivo do projeto é evitar bloqueios ao realizar scraping em massa. Para isso, o script em `manager_proxies.py` faz a gestão das proxies contidas no arquivo `proxie.txt`. O sistema testa automaticamente as proxies e marca aquelas que estão boas ou bloqueadas.

### Exemplo de Uso
1. Adicione suas proxies no arquivo `proxie.txt` com o formato `ip:port:username:password`.
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

## Contato

Se tiver dúvidas, sugestões ou apenas quiser trocar uma ideia sobre o projeto, entre em contato!

- [Meu LinkedIn](https://www.linkedin.com/in/bernardo-alemar/)
- [GitHub](https://github.com/bAlemar)

Fique à vontade para abrir uma issue ou enviar um PR com melhorias!

## Contribuindo

Pull requests são bem-vindos! Sinta-se à vontade para contribuir com melhorias no código, novas funcionalidades ou até mesmo ajustes na documentação. Para grandes mudanças, por favor, abra uma issue primeiro para discutir o que você gostaria de mudar.
