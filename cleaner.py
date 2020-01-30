import requests
import pandas as pd


def collect_df(url):
    """
    Takes in a url and returns a dataframe.
    Will rerport error if url did not result in 200 status code.
    """
    request = requests.get(url)
    if (request.status_code == 200):
        with request as f:
            raw = f.json()
        return pd.DataFrame(raw)
    else:
        print(f"Please enter a valid url. {request.status_code}")


def sgr_to_numeric(pdseries):
    """
    A simple function converting relative measures into numeric.
    The way it converts is as follows:
    FAR ABOVE AVERAGE = 4
    ABOVE AVERAGE = 3
    AVERAGE = 2
    BELOW AVERAGE = 1

    """
    for i in pdseries:
        if i == 'FAR ABOVE AVERAGE':
            pdseries.replace('FAR ABOVE AVERAGE', 4, inplace=True)
        elif i == 'ABOVE AVERAGE':
            pdseries.replace('ABOVE AVERAGE', 3, inplace=True)
        elif i == 'AVERAGE':
            pdseries.replace('AVERAGE', 2, inplace=True)
        elif i == 'BELOW AVERAGE':
            pdseries.replace('BELOW AVERAGE', 1, inplace=True)
    return pdseries