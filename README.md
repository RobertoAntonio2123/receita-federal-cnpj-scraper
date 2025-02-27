# WebScraper-CNPJ

##  Visão Geral
Este projeto tem como objetivo automatizar o processo de download, extração e limpeza de arquivos contendo informações de CNPJ. Ele segue uma estrutura modular, garantindo organização e facilidade de manutenção.

## Estrutura do Projeto
```
/webscraper-cnpj
│── /data                   # Armazena os dados brutos e limpos
│   ├── raw/                # Arquivos brutos baixados
│   ├── cleaned/            # Arquivos limpos
│── /src                      
│   ├── /services             
│   │   ├── downloader.py     # Faz o download do arquivo ZIP
│   │   ├── extractor.py      # Extrai o ZIP
│   │   ├── cleaner.py        # Faz a limpeza dos dados
│   │   ├── saver.py          # Salva o arquivo limpo
│   ├── /utils                
│   │   ├── date_handler.py   # Calcula o mês anterior corretamente
│   ├── config.py             # Configurações do projeto
│   ├── main.py               # Script principal
│── requirements.txt          # Dependências do projeto
│── README.md                 # Documentação do projeto
│── .gitignore                # Arquivos a serem ignorados pelo Git
```



###  Configuração do Ambiente
Certifique-se de ter o Python instalado. Em seguida, instale as dependências:
```bash
pip install -r requirements.txt
```

### 2Executando o Projeto
Para rodar o web scraper, basta executar o script principal:
```bash
python src/main.py
```

## ⚙️ Funcionamento
1. **Downloader**: Baixa o arquivo ZIP contendo os dados de CNPJ.
2. **Extractor**: Extrai os arquivos CSV do ZIP.
3. **Cleaner**: Realiza a limpeza dos dados, removendo colunas desnecessárias e filtrando registros inválidos.
4. **Saver**: Salva os arquivos limpos na pasta `/data/cleaned/`.

## 🛠 Tecnologias Utilizadas
- **Python** 
- **Pandas** 
- **Requests** 
- **OS & shutil** 

##  Autor
Projeto desenvolvido para automação de manipulação de dados de CNPJ. Se precisar de melhorias ou sugestões, contribua! 

