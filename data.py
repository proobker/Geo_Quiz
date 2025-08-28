import pandas
import os

class Data():
    def __init__(self):
        self.df = ""
        self.location = ""
        self.csv = None
        self.state = []
        self.total = 0
    
    def load(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.location = os.path.join(script_dir, self.df)
        self.csv = pandas.read_csv(self.location)
        self.state = list(self.csv['state'])
        self.total = len(self.state)
        
    def check(self, text):
        return text.lower() in self.csv['state'].str.lower().values
    
    def getx(self, text):
        text = text.lower()
        return int(self.csv[self.csv['state'].str.lower() == text]['x'].values[0])

    def gety(self, text):
        text = text.lower()
        return int(self.csv[self.csv['state'].str.lower() == text]['y'].values[0]) 
    
    def rmv(self, text):
        self.csv.drop(
            self.csv[self.csv['state'].str.lower() == text.lower()].index,
            inplace=True
        )