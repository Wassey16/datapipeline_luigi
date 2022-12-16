#!/home/my/virtual/bin/python
import os
import shutil
import luigi
from packages.datapush import datapush

if os.path.exists('tmp'):
    shutil.rmtree('tmp', ignore_errors=False, onerror=None)

if __name__ == '__main__':
    luigi.build([datapush()], workers=1,
                                    local_scheduler=True, detailed_summary=True, log_level='INFO')


  
  
  

  
   
# source /home/wassey/Documents/docker-com/luigi_datapipeline/my_venv/bin/activate && /home/wassey/Documents/docker-com/luigi_datapipeline/ && python /home/wassey/Documents/docker-com/luigi_datapipeline/main.py --local-scheduler datapush
#source /home/wassey/Documents/docker-com/luigi_datapipeline/my_venv/bin/activate && cd /home/wassey/Documents/docker-com/luigi_datapipeline/ && python /home/wassey/Documents/docker-com/luigi_datapipeline/main.py --local-scheduler datapush
