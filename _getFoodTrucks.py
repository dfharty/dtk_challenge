import requests
import logging
import _databaseLibrary as db

# should be from a config in the real world
sf_url = "https://data.sfgov.org/resource/rqzj-sfat.json?facilitytype=Truck"
# should be stored encrypted in the real world
token = "WDj6d8uOiV5d5VeFPaGXGF448"
logger = logging.getLogger(__name__)
logging.basicConfig(filename='challenge.log', encoding='utf-8', level=logging.DEBUG)

try:
    r = requests.get(sf_url, headers={'X-App-Token': token})
    msg = "{} called".format(r.url)
    logger.info(msg)
    msg = "{} status code returned".format(r.status_code)
    logger.debug(msg)
    if r.status_code == 200:
        trucks = r.json()
        result = db._make_table()
        if result == "SUCCESS":
            result = db._clear_trucks_table()
            if result == "SUCCESS":
                for truck in trucks:
                    sf_objectid = truck.get('objectid',"")
                    applicant = '"' + truck.get('applicant',"").replace("'"," ") + '"'
                    address = '"' + truck.get('address',"") + '"'
                    latitude = '"' + truck.get('latitude',"") + '"'
                    longitude = '"' + truck.get('longitude',"") + '"'
                    locationdescription = '"' + truck.get('locationdescription',"").replace(":","\\:") + '"'
                    fooditems = '"' + truck.get('fooditems',"").replace(":"," ") + '"'
                    status = '"' + truck.get('status',"") + '"'
                    result = db._load_trucks_table(sf_objectid, applicant,address,latitude,longitude,locationdescription,fooditems,status)
    else:
        msg = "ERROR: {} status code returned".format(r.status_code)
        logger.error(msg)

except Exception as e:
    logger.error(e)

