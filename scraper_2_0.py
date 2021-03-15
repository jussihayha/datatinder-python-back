import sys
import os
import time
import json
import requests
from dotenv import load_dotenv
from filter_extra_data import create_dated_json_filename, open_json, save_json


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
    count = 0
    while True:
        combined_url = url+parameters+str(offset)
        print(combined_url)

        results = requests.get(combined_url).json()
        count = results['meta']['count']
        time.sleep(12)

        if offset == 0:
            new_file = create_dated_json_filename("unfiltered")
            with open(new_file, "w") as f:
                json.dump(results['data'], f)

        else:
            existing_file = create_dated_json_filename("unfiltered")
            with open(existing_file) as f:
                curr_data = json.load(f)
                for i in range(len(results['data'])):
                    curr_data.append(results['data'][i])

                with open(existing_file, "w") as f:
                    json.dump(curr_data, f)

        if offset > count or offset == count:
            break
        else:
            offset += 100


def init():
    """ Initializes main-function. Used for achieving 100% test coverage """
    if __name__ == '__main__':
        sys.exit(main())


init()
