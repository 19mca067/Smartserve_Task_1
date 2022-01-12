from urllib.request import urlopen
import pandas as pd
import json


if __name__ == '__main__':
    api = 'https://s3.amazonaws.com/open-to-cors/assignment.json'
    data = json.loads(urlopen(api).read())
    data = data['products']
    df = pd.DataFrame(data)
    df = df.T
    df.to_csv('data.csv')
