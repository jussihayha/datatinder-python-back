""" Helper script for filtering data from a JSON-file to a new file """
import sys
import json
from helpers import create_dated_json_filename, open_json, save_json


class Program(object):
    def __init__(self, dict):
        self.id = get_id(self, dict)
        self.title = get_title(self, dict)
        self.description = get_description(self, dict)
        self.transmissio_title = get_transmission_title(self, dict)
        self.part_of_series = get_part_of_series(self, dict)
        self.genres = get_genres(self, dict)
        self.publication_event = get_publication_event(self, dict)
        self.image_id = get_image_id(self, dict)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def get_id(self, dict):
    """ Returns movie_id if available from JSON-data """
    try:
        return dict['id']
    except KeyError:
        return ''


def get_genres(self, dict):
    """ Returns genres in an array to object """
    temp_array = []
    for i in range(len(dict['subject'])):
        temp_array.append(dict['subject'][i]['title']['fi'])

    return temp_array


def get_title(self, dict):
    """ Returns title from object.
    First tries finnish, if does not exist then gets swedish title """
    try:
        return dict['title']['fi']
    except KeyError:
        return dict['title']['sv']


def get_transmission_title(self, dict):
    """ Returns transmissionTitle from object if available """
    try:
        return dict['transmissionTitle']
    except KeyError:
        return ''


def get_part_of_series(self, dict):
    """ Returns alternative_name from object if available """
    try:
        newObject = {
            "description": dict['partOfSeries']['description']['fi'],
            "shortDescription": dict['partOfSeries']['shortDescription']['fi']
        }
        return newObject
    except KeyError:
        return ''


def get_publication_event(self, dict):
    """ Returns current publication event used for streaming ondemand """
    try:
        for item in enumerate(dict['publicationEvent']):
            if item[1]['temporalStatus'] == 'currently':
                return item[1]
    except KeyError:
        return ''


def get_image_id(self, dict):
    """ Returns image ID, if available """
    try:
        return dict['image']
    except KeyError:
        return ''


def get_description(self, dict):
    """ Returns description of the object, if available """
    try:
        return dict['description']
    except KeyError:
        return ''


def main():
    """ Main-function, that starts script """
    filter_extra_data()
    print("Job complete")


def filter_extra_data():
    """ Filter unused data from JSON-file and return a cleaned JSON-file """
    combined_array = []
    unfiltered_file = open_json("unfiltered")
    for program in unfiltered_file:
        program = Program(program)
        combined_array.append(program.toJSON())
    save_json(combined_array, "filtered")


def init():
    """ Initializes main-function. Used for achieving 100% test coverage """
    if __name__ == '__main__':
        sys.exit(main())


init()
