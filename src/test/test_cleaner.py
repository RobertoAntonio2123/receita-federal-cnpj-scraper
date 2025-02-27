import os
from src.services.cleaner import clean_data
from src.utils.date_handler import get_last_month

if __name__ == "__main__":
    last_month = get_last_month()
    extracted_folder = f"extracted_{last_month}"
    cleaned_folder = f"cleaned_{last_month}"

    print(f"Limpando dados de {extracted_folder} para {cleaned_folder}...")
    clean_data(extracted_folder, cleaned_folder)
