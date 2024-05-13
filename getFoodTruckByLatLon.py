import _databaseLibrary as db
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='challenge.log', encoding='utf-8', level=logging.DEBUG)


# retrieves a food truck based on the combination of latitude and longitude
def getFoodTruckByLatLon(latitude, longitude):
    results = db._get_food_truck_lat_lon(latitude, longitude)
    msg = "getFoodTruckByLatLon: applicant: {} address {}".format(latitude,longitude)
    logger.debug(msg)
    return results
