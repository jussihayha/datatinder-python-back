# DataTinder python-backend

Currently executed manually as per needed.

## Used modules / packages
 - pymongo
 - json
 - python-dotenv

## Future enhancements
 - setup task to crontab to automatically run
 - fix scripts so that all filenames are set and opened dynamically
 - document scripts properly

## Key things to know
 - update_to_mongo.py does not do any checks if data already exists in collection
 - scraper_2.0.py still needs some manual love - should be fixed so that checks metadata to evaluate offset
 - combine_arrays_to_one.py is not currently needed but saved for convenience
 
