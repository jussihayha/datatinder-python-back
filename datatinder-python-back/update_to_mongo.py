""" Updates data to MongoDB """
import sys
import os
import json
from pymongo import MongoClient
from dotenv import load_dotenv
#from filter_extra_data import open_json

def main():
    """ Start script, print when done """
    load_dotenv()
    #send_data()
    if sys.argv[1] == "print":
        print_data()

def connect():
    """ Should be generalized so that you can send atleast database and
    collection as parameters """
    url = os.getenv('MONGO_URL')
    client = MongoClient(url)

    collection = client.YLE.rajapinta

    return collection


def open_json():
    """ Opens JSON-file and returns it as a variable
    To be replaced with function from imports """
    with open("2021-02-16-filtered.json", "r") as data:
        json_data = json.load(data)
        return json_data
    return

def send_data():
    """ First gets data from file, then connects to MongoDB and sends data to collection """
    json_data = open_json()
    client = connect()

    for item in json_data:
        client.insert_one(item)

    print("Data has been updated!")

def print_data():
    """ Returns some data from MongoDB - used for debugging """
    client = connect()

    for document in client.find():
        print(document['id'])

    print("Work complete!")

def get_single_program(sys.argv[1):
    """ Returns single program """
    client = connect():


def init():
    """ Initializes main-function. Used for achieving 100% test coverage"""
    if len(sys.argv) < 2:
        print("Insert either ID, or 'update' to update data")
        sys.exit()
    if __name__ == '__main__':
        sys.exit(main())
init()
