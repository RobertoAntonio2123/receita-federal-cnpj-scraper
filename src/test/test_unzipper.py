import os
from src.services.unzipper import extract_zip_file
from src.utils.date_handler import get_last_month

if __name__ == "__main__":
    last_month = get_last_month()
    zip_file = f"data_{last_month}.zip"
    extract_path = f"extracted_{last_month}"

    print(f"Extraindo {zip_file} para {extract_path}...")
    extract_zip_file(zip_file, extract_path)
