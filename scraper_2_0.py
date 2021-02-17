import sys
import time
import json
import requests
import os
from dotenv import load_dotenv
from filter_extra_data import get_curr_date, open_json, save_json

def main():
    """ Starts script """
    load_dotenv()
    fetch_data()
    print("Job complete")

def fetch_data():
    """ Fetches data from YLE-api and saves to file """
    url = os.getenv('YLE_API_URL')
    parameters = "&category=5-131&availability=ondemand&mediaobject=video&type=program&region=fi&offset=" 
    offset = 0
    
    while True:
        combined_url = url+parameters+str(offset)
        print(combined_url)

        results = requests.get(combined_url).json()
        
        time.sleep(12)

        if offset == 0:
            new_file = get_curr_date("unfiltered")
            with open(new_file, "w") as f:
                json.dump(results['data'], f)

        else:
            existing_file = get_curr_date("unfiltered")
            with open(existing_file) as f:
                currData = json.load(f)
                for i in range(len(results['data'])):
                    currData.append(results['data'][i])

                with open(existing_file, "w") as f:
                    json.dump(currData, f)

        if offset == 2500:
            break
        else:
            offset += 25

def init():
    """ Initializes main-function. Used for achieving 100% test coverage """
    if __name__ == '__main__':
        sys.exit(main())

init()
