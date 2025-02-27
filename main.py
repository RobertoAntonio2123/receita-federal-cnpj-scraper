### src/main.py
#from utils.date_handler import get_last_month
from src.utils.date_handler import get_last_month
from src.services.downloader import baixar_arquivo_zip
from src.services.extractor import extract_zip_file
from src.services.cleaner import clean_data
import os
from src.config import DATA_RAW_DIR, DATA_CLEANED_DIR

def main():
    last_month = get_last_month()
    url = f"https://portaldatransparencia.gov.br/download-de-dados/favorecidos-pj/{last_month}"
    zip_path = os.path.join(DATA_RAW_DIR, f"dados_{last_month}.zip")
    extracted_folder = os.path.join(DATA_RAW_DIR, f"dados_{last_month}")
    
    baixar_arquivo_zip(url, zip_path)
    extract_zip_file(zip_path, extracted_folder)
    clean_data(extracted_folder, DATA_CLEANED_DIR)

if __name__ == "__main__":
    main()

