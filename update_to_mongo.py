""" Updates data to MongoDB """
import sys
import os
from pymongo import MongoClient
from dotenv import load_dotenv
from filter_extra_data import open_json


def main():
    """ Start script, print when done """
    load_dotenv()

    if len(sys.argv) == 2 and sys.argv[1] == 'print':
        print_data()

    if len(sys.argv) == 3 and sys.argv[1] == 'id':
        get_single_program(sys.argv[2])

    if len(sys.argv) == 2 and sys.argv[1] == 'update':
        confirm = input("Are you sure you want to update the DB? Y/N?")
        if confirm.upper() == "Y":
            update_data()


def connect():
    """ Should be generalized so that you can send atleast database and
    collection as parameters """
    url = os.getenv('MONGO_URL')
    client = MongoClient(url)

    return client


def update_data():
    """ First gets data from file, then connects to MongoDB and sends data to collection """
    json_data = open_json("filtered")
    client = connect()
    with connect() as client:
        collection = client.YLE.rajapinta
        for item in json_data:
            # (filter, replacement, upsert)
            # if collection has object with same id as item['id'] -> update data
            # else creates new object.
            collection.replace_one({'id': str(item['id'])}, item, True)

    print("Data has been updated!")


def print_data():
    """ Returns some data from MongoDB - used for debugging """
    with connect() as client:
        collection = client.YLE.rajapinta
        for document in collection.find():
            print(document['id'])
    print("Work complete!")


def get_single_program(movie_id):
    """ Returns single program """
    with connect() as client:
        collection = client.YLE.rajapinta
        document = collection.find_one({"id": str(movie_id)})
    print(document)


def init():
    """ Initializes main-function. Used for achieving 100% test coverage"""
    if len(sys.argv) < 2:
        print("Insert either ID, or 'update' to update data")
        sys.exit()
    if __name__ == '__main__':
        sys.exit(main())


init()
