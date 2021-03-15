""" Helper script for filtering data from a JSON-file to a new file """
import json
import sys
from datetime import date


class Program:
    def __init__(self, id, title, description, transmission_title, part_of_series, genres, publication_event, image_id):
        self.id = id
        self.title = title
        self.description = description
        self.transmissio_title = transmission_title
        self.part_of_series = part_of_series
        self.genres = genres
        self.publication_event = publication_event
        self.image_id = image_id


def main():
    """ Main-function, that starts script """
    filter_extra_data()
    print("Job complete")


def filter_extra_data():
    """ Filter unused data from JSON-file and return a cleaned JSON-file """
    combined_array = []
    unfiltered_file = open_json("unfiltered")
    for i in range(len(unfiltered_file)):
        movie_object = {
            "id": set_id(unfiltered_file[i]),
            "title": set_title(unfiltered_file[i]),
            "description": set_description(unfiltered_file[i]),
            "transmission_title": set_transmission_title(unfiltered_file[i]),
            "part_of_series": set_part_of_series(unfiltered_file[i]),
            "genres": set_genres(unfiltered_file[i]),
            "publication_event": set_publication_event(unfiltered_file[i]),
            "image_id": set_image_id(unfiltered_file[i])
        }
        combined_array.append(movie_object)
    save_json(combined_array, "filtered")


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


def set_id(movie):
    """ Returns movie_id if available from JSON-data """
    try:
        return movie['id']
    except KeyError:
        return ''


def set_genres(movie):
    """ Returns genres in an array to object """
    temp_array = []
    for i in range(len(movie['subject'])):
        temp_array.append(movie['subject'][i]['title']['fi'])

    return temp_array


def set_title(movie):
    """ Returns title from object.
    First tries finnish, if does not exist then gets swedish title """
    try:
        return movie['title']['fi']
    except KeyError:
        return movie['title']['sv']


def set_transmission_title(movie):
    """ Returns transmissionTitle from object if available """
    try:
        return movie['transmissionTitle']
    except KeyError:
        return ''


def set_part_of_series(movie):
    """ Returns alternative_name from object if available """
    try:
        newObject = {
            "description": movie['partOfSeries']['description']['fi'],
            "shortDescription": movie['partOfSeries']['shortDescription']['fi']
        }
        return newObject
    except KeyError:
        return ''


def set_publication_event(movie):
    """ Returns current publication event used for streaming ondemand """
    try:
        for item in enumerate(movie['publicationEvent']):
            if item[1]['temporalStatus'] == 'currently':
                return item[1]
    except KeyError:
        return ''


def set_image_id(movie):
    """ Returns image ID, if available """
    try:
        return movie['image']
    except KeyError:
        return ''


def set_description(movie):
    """ Returns description of the object, if available """
    try:
        return movie['description']
    except KeyError:
        return ''


def init():
    """ Initializes main-function. Used for achieving 100% test coverage """
    if __name__ == '__main__':
        sys.exit(main())


init()
