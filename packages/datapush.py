import luigi
from pakags.clean import dataclean
import pandas as pd 
from sqlalchemy import create_engine

class datapush(luigi.Task):
    def requires(self):
        return dataclean()
    def run(self):

        engine = create_engine("postgresql://bob:admin@localhost:5432/mydb")
        data = pd.read_csv(self.input().open('r'))
        data.to_sql('nyc_station', con=engine, if_exists='replace')

if __name__ == "__main__":
    luigi.run()
