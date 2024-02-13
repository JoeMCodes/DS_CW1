### This file will download the data and create a json file in data/raw and 

import urllib.request
import gzip
import json

url = 'https://atlantides.org/downloads/pleiades/json/pleiades-places-latest.json.gz'  ## This url could change
output_file = '../../data/raw/pleiades-places-latest.json'

# Download the compressed JSON file
urllib.request.urlretrieve(url, '../../data/raw/pleiades-places-latest.json.gz')

# Decompress the file and save the JSON data
with gzip.open('../../data/raw/pleiades-places-latest.json.gz', 'rb') as f_in:
    with open(output_file, 'wb') as f_out:
        f_out.write(f_in.read())
