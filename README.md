# luigi_datapipeline 
A webpage about nyc station is scrapped. Its data converted from json to csv, cleaned and exported into a table in a postgresql data base.

### Requirements:
* install `python3` 
* install `docker` for `postgres` 

### Dependencies :
* for all the dependencies run `source scripts/setup.sh` in terminal
* for seting up postgres run `scripts/run_db.sh` to stop run `scripts/stop_db.sh`

 
### Running:
to run luig UI in terminal:
```bash
sudo ufw allow 8082/tcp
sudo sh -c ". my_venv/bin/activate ;luigid --background --port 8082 
luigid --port 8082 > /dev/null 2> /dev/null &
python -m luigi --module main datapush
```
to see the UI in broweser type `http//localhost:8082` and to kill luigid in terminal:
```bash 
sudo netstat -lpn |grep :8082
kill -9 "your_procces_id"
```
to run task once in terminal:
```bash
python3 main.py
```
to run test to check the success of luigi task in terminal:
```bash
python3 test.py 
```

to run as a cronjob task give your path to `cd` in cron.sh and in new terminal:
```bash
chmod +x scripts/cron.sh
EDITOR=nano crontab -e
```
this will open crontab write the following command in the editor to run job every day at 15:15 
```bash
15 15 * * * /bin/bash complete_path_to/luigi_datapipeline/scripts/cron.sh
```

### Functionality:
* luigi task `scrap()` extracts the data in cleaned up json format.
* luigi task `convert()` pretifies and changes the format from json to csv.
* luigi task `dataclean()` uses pandas to cleanup the data. 
* luigi task `datapush()` pushes data into a table in postgresql database present on local machine.

