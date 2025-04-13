import os
from zipfile import ZipFile
import pytest

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')
RES_DIR = os.path.join(CURRENT_DIR, 'resources')
file_dir = os.listdir(TMP_DIR)


# Создание архива
@pytest.fixture(scope='function', autouse=True)
def create_archive():
    if not os.path.exists('resources'):
        os.mkdir('resources')

    with ZipFile('resources/companies.zip', 'w') as my_zip:
        for file in file_dir:
            add_file = os.path.join('tmp', file)
            my_zip.write(add_file)
