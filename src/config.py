import os
from src.utils.date_handler import DateHandler


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_RAW_DIR = os.path.join(BASE_DIR, "data", "raw")  # Diretório dos arquivos brutos
DATA_CLEANED_DIR = os.path.join(BASE_DIR, "data", "cleaned")  # Diretório dos arquivos limpos
ARQUIVO_RAW = os.path.join(DATA_RAW_DIR, "dados_brutos.csv")  # Nome do arquivo bruto
ARQUIVO_LIMPO = os.path.join(DATA_CLEANED_DIR, "dados_limpos.csv")  # Nome do arquivo limpo

# Diretórios principais
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# URL para download
ANO_MES_ATUAL = DateHandler.obter_ano_mes_atual()
URL_DOWNLOAD = f"https://portaldatransparencia.gov.br/download-de-dados/favorecidos-pj/{ANO_MES_ATUAL}"

# Caminhos dos arquivos
ARQUIVO_RAW = os.path.join(DATA_RAW_DIR, f"{ANO_MES_ATUAL}_CNPJ.csv")
ARQUIVO_LIMPO = os.path.join(DATA_CLEANED_DIR, f"{ANO_MES_ATUAL}_CNPJ_LIMPO.csv")
