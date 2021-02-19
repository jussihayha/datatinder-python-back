# DataTinder python-backend

Currently executed manually as per needed.

## Used modules / packages
 - pymongo
 - json
 - python-dotenv
 - request
 - sys
 - os
 - time
 - datetime
 
## Scripts in a nutshell
### Usage
 - You need to install python-dotenv and set the following variables to it:
   YLE_API_URL = "https://external.api.yle.fi/v1/programs/items.json?app_id=<YOUR_APPID>&app_key=<YOUR_APP_KEY>
   MONGO_URL = "mongodb+srv://<username>:<password>@<project_url>/<database>?retryWrites=true"
- Collection has been hardcoded in update_to_mongo.py - so check that out also.

#### scraper_2_0.py
- Simple while-loop that gets data from YLE API. 
- YLE API restricts your queries, so that you only get 25 responses at a time.
- The script checks for 'count' value in the response, that tells how many items there are altogether. Count value is compared to offset-value that increments after every iteration. If offset exceeds count or is the same, there is no more new objects for you to get.

#### filter_extra_data.py
- Filters data that has been fetched with scraper_2.0.py.
- Saves data to a new file. 
- Assumes that will be run during the same day as scraper_2.0.py.
  
#### combine_arrays_to_one.py
- Saved in this repo for convenience.
## Future enhancements
 - Setup task to crontab to automatically run.
 - Fix scripts so that all filenames are set and opened dynamically.
 - Add command line parameters to update_to_mongo, so that can be used also for fetching data for debugging purposes. 
