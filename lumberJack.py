import pandas as pd

class lumberJack:

    def __init__(self, name, columns):
        self.columns = columns
        self.name = name
        self.filename = name+'_log.csv'
        self.data = []
        
        #st = ''
        #for i in self.columns:
        #    st += ',{}'.format(i)
        
        #f = open(self.filename, 'w')
        #f.write(st)
        #self.data.append(columns)
        #f.close()

    def log(self, event_details):
        if len(event_details) == len(self.columns):
            print('{}: Dimensions check out.'.format(self.name))
            self.data.append(event_details)

            df = pd.DataFrame.from_records(self.data, columns=self.columns)
            #print(df)
            df.to_csv(self.filename)
            
        else:
            print('Recieved data with dimensions not matching logger dimensions. Expected {}, got {}.'.format(len(self.columns), len(event_details)))
            
    def export(self):
        df = pd.DataFrame.from_records(self.data, columns=self.columns)
        #print(df)
        df.to_csv(self.filename)
        return df