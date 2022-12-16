import luigi 
import pandas as pd 
from packages.convert import convert

class dataclean(luigi.Task):
    def requires(self):
        return convert()

    def output(self):
        return luigi.LocalTarget("tmp/formated.csv")
    
    def run(self):
        df = pd.read_csv(self.input().open('r'))
        x = df[["name","lat","lon"]]
        x = x[:1001]
        y =  x.to_csv(index=False)
        f = self.output().open('w')
        f.write(y)
        f.close()

if __name__ == "__main__":
    luigi.run()
