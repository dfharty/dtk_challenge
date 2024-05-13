# Dave Harty's What The Truck Challenge
Assumptions:
It was described as interest in food trucks to the url to collect the data has a filter parameter to only retrieve trucks. This could be changed if one wanted to include the "e-coli carts" but most Doctors would not recommend it

To reel back in my scope-creep, which was embarrassingly out of control, this has been limited to serving as a backend set of APIs for a Front End developer to consume.

Based on the limited size of the data a snapshot approach was used to collect the data daily.

Basic unit tests were provided, integration tests were ignored for simplicity of the task.

Requirements:
* Built with Python 3.12
* Uses requests for accessing SODA site
* Implements SQLite3 locally for simplicity of the task
* Logging to local file for simplicity of the task
* Implements internal calls with a preceding underscore which in Python restricts nothing but conveys to the user that they are meant to be internal use only

You can command line with python _getFoodTrucks.py to get the latest list of trucks and store them

Unit tests can be run from python /tests/unit_tests/database_tests.py






