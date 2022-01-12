# imported libraries
from urllib.request import urlopen
import pandas as pd
import json


if __name__ == '__main__':  # main statement
    # link to dataset file in json format
    api = 'https://s3.amazonaws.com/open-to-cors/assignment.json'
    # loading the dataset from json object
    data = json.loads(urlopen(api).read())
    # using required field objects from dataset and removing count column
    data = data['products']
    # Converting the dataset in json to pandas dataframe structure
    df = pd.DataFrame(data)
    # Taking transpose of dataframe to convert row to column and vice versa
    df = df.T
    # Writing final data to data.csv file
    df.to_csv('data.csv')
