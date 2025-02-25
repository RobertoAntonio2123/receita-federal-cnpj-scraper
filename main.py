from src.services.downloader import baixar_arquivo_zip
from src.services.extractor import extrair_arquivo_zip
from src.services.cleaner import limpar_dados
from src.services.saver import mover_arquivo
from src.config import URL_DOWNLOAD, DATA_RAW_DIR, DATA_CLEANED_DIR, ARQUIVO_RAW, ARQUIVO_LIMPO

def main():
    print("Iniciando processo de extração e limpeza de dados...")

    # Baixar o arquivo ZIP
    conteudo_zip = baixar_arquivo_zip(URL_DOWNLOAD)
    if conteudo_zip:
        extrair_arquivo_zip(conteudo_zip, DATA_RAW_DIR)

        # Limpar os dados
        limpar_dados(ARQUIVO_RAW, ARQUIVO_LIMPO)

        # Mover arquivo limpo para pasta cleaned
        mover_arquivo(ARQUIVO_LIMPO, f"{DATA_CLEANED_DIR}/{ARQUIVO_LIMPO}")

if __name__ == "__main__":
    main()
