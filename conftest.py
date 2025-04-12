import os
from zipfile import ZipFile

import pytest

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')
file_dir = os.listdir(TMP_DIR)

@pytest.fixture(scope='function', autouse=True)
def create_folder():
    if not os.path.exists('resources'):
        os.mkdir('resources')

@pytest.fixture(scope='function', autouse=True)
def create_zip():
    with ZipFile('resources/companies.zip', 'w') as my_zip:
        for file in file_dir:
            add_file = os.path.join('tmp', file)
            my_zip.write(add_file)