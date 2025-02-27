from src.services.downloader import baixar_arquivo_zip
from src.utils.date_handler import get_last_month  # Certifique-se de que a função está disponível

if __name__ == "__main__":
    last_month = get_last_month()
    url = f"https://portaldatransparencia.gov.br/download-de-dados/favorecidos-pj/{last_month}"
    save_path = f"data_{last_month}.zip"
    
    print(f"Baixando: {url}")
    baixar_arquivo_zip(url)
