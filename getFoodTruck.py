import _databaseLibrary as db
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(filename='challenge.log', encoding='utf-8', level=logging.DEBUG)

# retrieves a food truck based on the combination of permit applicant and address
def getFoodTruck(applicant, address):
    results = db._get_food_truck(applicant, address)
    msg = "getFoodTruck: applicant: {} address {}".format(applicant,address)
    logger.debug(msg)
    print(results)
    return results


if __name__ == '__main__':
    db._get_food_truck("'Truck McTruckster'", "'1234 Main Street'")
    # getFoodTruck("'Ruru Juice LLC'", "'601 MISSION ST'")