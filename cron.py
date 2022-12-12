import os
import time 
import schedule 
def job():
    os.system('python -m luigi --module main datapush --local-scheduler')
schedule.every().day.at("15:00").do(job)

if __name__=='__main__':
    while True:
        schedule.run_pending()
        time.sleep(1)
