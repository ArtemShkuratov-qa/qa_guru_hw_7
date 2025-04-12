import os
import csv
import zipfile

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')
RES_DIR = os.path.join(CURRENT_DIR, 'resources')
file_dir = os.listdir(TMP_DIR)

def test_csv():
    with zipfile.ZipFile(os.path.join(RES_DIR, 'companies.zip')) as zf:
        with zf.open('tmp/import_company_csv.csv') as csv_file:
            content = csv_file.read().decode('utf-8-sig')
            csvreader = list(csv.reader(content.split()))  # читаем содержимое файла и преобразуем его в список
            second_row = csvreader[1]  # получаем вторую строку
            print(csvreader)
            print(second_row)
            #assert second_row[0] == 'OU001'  # проверка значения элемента в первом столбце второй строки
            #assert second_row[2] == 'ЗАО"Сервис"'

