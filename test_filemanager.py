from victorina import viktorina
import random
def test_viktorina():
    names = {1: 'H Kolumb', 2: 'A Enchtein',
             3: 'A Puchkin', 4: 'L Paster',
             5: 'G Galilei', 6: 'W Shekspir',
             7: 'L De Vinchi', 8: 'A Mozart',
             9: 'I Newton', 10: 'G Leibniz'
             }
    numbers = [names[1], names[2], names[3], names[4], names[5], names[6], names[7], names[8], names[9], names[10]]
    result = random.sample(numbers, 5)
    assert len(result) == 5
from manager import choice
import os
import shutil
if choice == '3':
    dir_name = f'new'
    os.path.exists(dir_name)
    copy_dir_name = f'copy_new'
    assert shutil.copy(dir_name, copy_dir_name)

from bank_account import account
bill_sum = 10
cost = 5
if bill_sum > cost:
    assert account > 0
