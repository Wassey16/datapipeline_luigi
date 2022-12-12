import luigi 
import json 
from packages.scrap import scrap
import csv 


class convert(luigi.Task):
    def requires(self):
        return scrap()


    def output(self):
            return luigi.LocalTarget("nycbikedata.csv")

            
    def run(self):

        #opening json file with data
        with self.input().open('r') as json_file:
            data = json.load(json_file)
        #all the data is in station object data.json file
        station = data['data']['stations']
        data_file = self.output().open('w')
        csv_writer = csv.writer(data_file)
        count = 0

        for x in station:
            if count == 0:
                # Writing headers of CSV file
                header = x.keys()
                csv_writer.writerow(header)
                count += 1

            # Writing data of CSV file
            csv_writer.writerow(x.values())

        data_file.close()
        
if __name__ == "__main__":
    luigi.run()
