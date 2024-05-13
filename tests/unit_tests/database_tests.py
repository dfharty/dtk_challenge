import time
import unittest
import _databaseLibrary as db


class TestDBMethods(unittest.TestCase):

    def test__load_trucks_table(self):
        result = db._load_trucks_table("'ZZZ999999'", "'Truck McTruckster'", "'1234 Main Street'", "'37.78767164448785'",
                                   "'-122.39976292583923'", "'Someplace nice with a water view'",
                                   "'Tootsie rolls: lots of Tootsie rolls'", "'PENDING'")
        self.assertEqual(result, "SUCCESS")

    def test__get_food_truck(self):
        result = db._get_food_truck("'Truck McTruckster'", "'1234 Main Street'")
        self.assertEqual(result[0], "Truck McTruckster")

    def test__get_food_truck_lat_lon(self):
        result = db._get_food_truck_lat_lon("'37.78767164448785'", "'-122.39976292583923'")
        self.assertEqual(result[0], "Truck McTruckster")


if __name__ == '__main__':
    unittest.main()