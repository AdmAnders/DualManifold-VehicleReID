import os
import zipfile

def extract_dataset():
    zip_file_path = '/...../Dataset/VeRi.zip'
    extract_to_path = '/content'

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_path)
        num_files = len(zip_ref.namelist())
    print(f"Total {num_files} Files.")







The rest of the code will be updated after the article is published.
