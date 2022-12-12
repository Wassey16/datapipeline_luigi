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
