""" All helper functions that are used in multiple functions """
from datetime import date
import json

def create_dated_json_filename(name):
    """ Returns current date combined with provided name """
    curr_date = date.today()

    return f"{curr_date}-{name}.json"


def open_json(name):
    """ Opens JSON-file and returns its content """
    unfiltered_file = create_dated_json_filename(name)

    with open(unfiltered_file, "r") as unfiltered:
        imported_json = json.load(unfiltered)

        return imported_json


def save_json(combined_array, name):
    """ Saves a new JSON-file """
    filtered_file = create_dated_json_filename(name)
    with open(filtered_file, "w") as filtered:
        json.dump(combined_array, filtered)
