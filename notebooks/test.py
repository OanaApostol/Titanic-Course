import os
import requests
from dotenv import load_dotenv, find_dotenv
import json

# find .env automatically by walking up directories until it's found
dotenv_path = find_dotenv()
# load up the entries as environment variables
load_dotenv(dotenv_path)

# payload for post
payload = {
    'username': os.environ.get("KAGGLE_USERNAME"),
    'password': os.environ.get("KAGGLE_PASSWORD")
}

# url for train file (get the link from Kaggle website)
url = 'http://www.kaggle.com/c/digit-recognizer/download/train.csv'

# login to kaggle and retrieve the data
r = requests.post(url, data = payload)
response = requests.get(url)
print(r)


with session() as c:
    # post requests
    c.post('https://www.kaggle.com', data=payload)
    # get request
    response = c.get(url)
    # print response text
    print(response.text)