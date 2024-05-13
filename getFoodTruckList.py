import _databaseLibrary as db
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='challenge.log', encoding='utf-8', level=logging.DEBUG)


def getFoodTruckList():
    results = db._read_trucks_table()
    count = len(results)
    msg = "getFoodTruckList: count: %d" % count
    logger.debug(msg)
    return results
