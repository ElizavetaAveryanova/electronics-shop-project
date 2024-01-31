import os.path
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

DICT_DIR = os.path.join(ROOT_DIR, 'src', 'items.csv')

DICT_DIR_NO_EXIST = os.path.join(ROOT_DIR, 'src', 'no_exist.csv')

DICT_DIR_BROKEN_1 = os.path.join(ROOT_DIR, 'src', 'items_broken.csv')

DICT_DIR_BROKEN_2 = os.path.join(ROOT_DIR, 'src', 'items_broken2.csv')