""" Helper script for filtering data from a JSON-file to a new file """
import json
import sys
from datetime import date

def main():
    """ Main-function, that starts script """
    filter_extra_data()
    print("Job complete")

def filter_extra_data():
    """ Filter unused data from JSON-file and return a cleaned JSON-file """
    combined_array = []
    unfiltered_file = open_json()
    for i in range(len(unfiltered_file)):
        movie_object = {
                "id": set_id(unfiltered_file[i]),
                "name": set_title(unfiltered_file[i]),
                "alternative_name": set_name(unfiltered_file[i]),
                "other_alternative_name": set_alternative_name(unfiltered_file[i]),
                "genres": set_genres(unfiltered_file[i]),
                "publication_event": set_publication_event(unfiltered_file[i])
                }
        combined_array.append(movie_object)
    save_json(combined_array)

def get_curr_date(name):
    """ Returns current date combined with provided name """
    curr_date = date.today()

    return f"{curr_date}-{name}.json"

def open_json():
    """ Opens JSON-file and returns its content """
    unfiltered_file = get_curr_date("unfiltered")

    with open (unfiltered_file, "r") as unfiltered:
        imported_json = json.load(unfiltered)

        return imported_json

def save_json(combined_array):
    """ Saves a new JSON-file """
    filtered_file = get_curr_date("filtered")
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
    """ Returns title from object if available """
    try:
        return movie['title']['fi']
    except KeyError:
        return movie['title']['sv']

def set_name(movie):
    """ Returns transmissionTitle from object if available """
    try:
        return movie['transmissionTitle']
    except KeyError:
        return ''

def set_alternative_name(movie):
    """ Returns alternative_name from object if available """
    try:
        return movie['partOfSeries']['title']['fi']
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

def init():
    """ Initializes main-function. Used for achieving 100% test coverage """
    if __name__ == '__main__':
        sys.exit(main())

init()
                                  