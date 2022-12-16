#!/usr/bin/env sh
cd /home/wassey/Documents/docker-com/luigi_datapipeline/
source my_venv/bin/activate
python -m luigi --module main datapush --local-scheduler
exec bash