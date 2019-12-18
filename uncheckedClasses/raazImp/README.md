DATA FILES
===================

This is still a WIP

Current Situation:
______

- You will need to "pip3 install pandas" before running any of the code
- The ta_lib_init.py file has been completed (no comments)
	- For documentation see:
		- chickenLittle.py (comments included)
		- The OneNote has each function documented and explained

______


File Guide:
----------

> "ta_lib_init.py"
-- This file has been completed. From this file the user must import the "TALIBINIT" function. This function takes in a data file(see dataManager.py) as a parameter and then returns a data file with all the technical indicators. This returned file should then be stored in an object or written to the disk using the ".to_csv" function(used in dataManager.py"

> "miscTest.py"
-- This file is just for testing. It passes a CSV file to the dataManager.py class. This is subject to continual change.

> "dataManager.py"
-- This file is currently being worked on. Right now it just tests the ta_lib_init.py file.

--------

All other files are WIP
