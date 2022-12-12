# datapipeline_luigi
A webpage about nyc station is scrapped. Its data converted from json to csv, cleaned and exported into a table in a postgresql data base.

### Requirements:
* install `python3` 
* install `docker` for `postgres` 

### Dependencies :
* for all the dependencies run `source scripts/setup.sh` in terminal
* for seting up postgres run `scripts/run_db.sh` to stop run `scripts/stop_db.sh`

 
### Running:
to run task once in terminal:
```bash
python3 main.py
```
to run test to check the success of luigi task in terminal:
```bash
python3 test.py 
```

to run as a scheduled task in terminal:
```bash
python3 cron.py
```
 
### Functionality:
* luigi task `scrap()` extracts the data in cleaned up json format.
* luigi task `convert()` pretifies and changes the format from json to csv.
* luigi task `dataclean()` uses pandas to cleanup the data. 
* luigi task `datapush()` pushes data into a table in postgresql database present on local machine.

