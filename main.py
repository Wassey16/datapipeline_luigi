import os
import luigi
from packages import datapush
if __name__=='__main__':
    os.system('python -m luigi --module main datapush --local-scheduler')