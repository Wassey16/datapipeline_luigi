#!/home/my/virtual/bin/python
import os
import shutil
import luigi
from packages import datapush

if os.path.exists('tmp_files'):
    shutil.rmtree('tmp_files', ignore_errors=False, onerror=None)

if __name__ == '__main__':
    os.system('python -m luigi --module main datapush --local-scheduler')
