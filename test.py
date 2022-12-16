import unittest
import psycopg2
import pandas as pd

def datacheck():
    hostname = 'localhost'
    database = 'mydb'
    username = 'bob'
    pwd      = 'admin'
    port_id  =  5432
    try:
        conn = psycopg2.connect(
                    host = hostname,
                    dbname = database,
                    user = username,
                    password = pwd,
                    port = port_id)
        cur = conn.cursor()
    
        create_script = '''SELECT * FROM nyc_station LIMIT 1; '''
        cur.execute(create_script)
        data=cur.fetchone()
        conn.commit()
    except Exception as error:
        print(error)
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
                conn.close()
    data = data[1:]
    x=data.__str__()
    x=x.replace("'",'').replace('(','').replace(')','') 


    return x

class LuigiTest(unittest.TestCase):
    def test_datapush(self):
        df=pd.read_csv('tmp/formated.csv')
        x=df.iloc[0]
        y = x.astype(str).values.flatten().tolist().__str__()
        y=y.replace('[','').replace(']','').replace("'",'')
        result = datacheck()
        self.assertEqual(result,y)




if __name__ =="__main__":
    unittest.main()
    
