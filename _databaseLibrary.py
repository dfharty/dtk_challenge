import logging
import sqlite3

logger = logging.getLogger(__name__)
logging.basicConfig(filename='challenge.log', encoding='utf-8', level=logging.DEBUG)
con = sqlite3.connect("sffoodtrucks.db")


def _make_table():
    # create table if it does not exist, will not overwrite if it does.
    logger.info("_make_table called")
    try:
        cur = con.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS sf_food_trucks (id INTEGER PRIMARY KEY AUTOINCREMENT, sf_objectid, applicant,address,"
            "latitude,longitude,locationdescription, fooditems, status)"
            )
    except Exception as e:  # normally would have several with more granular error trapping
        logger.error("Error in _make_table: {}".format(e))
        return "ERROR"
    cur.close()
    return "SUCCESS"  # Booleans would be cheaper but prefer the readability


def _clear_trucks_table():
    # Empty out the trucks table as we are doing a full snapshot refresh
    logger.info("_clear_trucks_table called")
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM sf_food_trucks")
        logger.debug("_clear_trucks_table called successfully")

    except Exception as e:  # normally would have several with more granular error trapping
        logger.error("Error in _clear_trucks_table: {}".format(e))
        return "ERROR"
    cur.close()
    con.commit()
    return "SUCCESS"  # Booleans would be cheaper but prefer the readability


def _delete_truck(sf_objectid):
    # delete a truck by id
    logger.info("_delete_truck called")
    try:
        cur = con.cursor()
        sql = "DELETE FROM sf_food_trucks WHERE sf_objectid={}".format(sf_objectid)
        print(sql)
        cur.execute(sql)
        logger.debug("_delete_truck called successfully")

    except Exception as e:  # normally would have several with more granular error trapping
        logger.error("Error in _delete_truck: {}".format(e))
        return "ERROR"
    cur.close()
    con.commit()
    return "SUCCESS"  # Booleans would be cheaper but prefer the readability

def _load_trucks_table(sf_objectid, applicant,address,latitude,longitude="",locationdescription="", fooditems="", status=""):
    # Insert food trucks. Normally we would look to simply find deltas for updates and not re-write the whole table
    logger.info("_load_trucks_table called")
    try:
        sql = ("INSERT INTO sf_food_trucks (sf_objectid, applicant,address,latitude,longitude,locationdescription, fooditems, status)"
               " VALUES({},{},{},{},{},{},{},{})").format(sf_objectid, applicant,address,latitude,longitude,locationdescription, fooditems, status)
        cur = con.cursor()
        cur.execute(sql)
        msg = "_load_trucks_table called successfully with SQL of : {}".format(sql)
        logger.debug(msg)

    except Exception as e:  # normally would have several with more granular error trapping
        logger.error("Error in _load_trucks_table: {}".format(e))
        return "ERROR"
    cur.close()
    con.commit()
    return "SUCCESS"  # Booleans would be cheaper but prefer the readability


def _read_trucks_table():
    # returns the full list of food trucks
    logger.info("_read_trucks_table called")
    cur = con.cursor()
    results = cur.execute(
        "SELECT applicant,address,"
        "latitude,longitude,locationdescription, fooditems, status FROM sf_food_trucks"
    )
    results = cur.fetchall()
    logger.debug("read_trucks_table called successfully - returned: {}".format(results))
    return results


def _get_food_truck(applicant: str, address: str):
    # get an individual food truck by name(applicant) and address (assumes applicants can have more than one truck)
    msg = "_get_food_truck called with applicant= {} and address={}".format(applicant, address)
    logger.info(msg)
    try:
        cur = con.cursor()
        sql = "SELECT applicant,address,latitude,longitude,locationdescription,fooditems,status FROM sf_food_trucks WHERE applicant ={} AND address ={}".format(str(applicant),str(address))
        cur.execute(sql)
    except Exception as e:  # normally would have several with more granular error trapping
        logger.error("Error in _load_trucks_table: {}".format(e))
        cur.close()
        return "ERROR"
    results = cur.fetchone()
    logger.debug("_get_food_truck returns: {}".format(results))
    cur.close()
    return results


def _get_food_truck_lat_lon(latitude, longitude):
    # get an individual food truck by lat/lon assumes no double-parking ;-)
    msg = "_get_food_truck called with latitude= {} and longitude={}".format(latitude, longitude)
    logger.info(msg)
    try:
        cur = con.cursor()
        sql= ("SELECT applicant,address, latitude,longitude,locationdescription, fooditems, status "
              "FROM sf_food_trucks "
              "WHERE latitude={} AND longitude={}").format(latitude, longitude)
        cur.execute(sql)

    except Exception as e:  # normally would have several with more granular error trapping
        logger.error("Error in _load_trucks_table: {}".format(e))
        cur.close()
        return "ERROR"
    results = cur.fetchone()

    logger.debug("_get_food_truck_lat_lon returns: {}".format(results))
    cur.close()
    return results
