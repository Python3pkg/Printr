# Import python modules
import os
from json import loads as json_loads

# Import Printr Modules
from .simplePrintr import SimplePrintr
from .itterPrintr import ItterPrintr
from .ellipsisPrintr import EllipsisPrintr

# Initialise
PRINTR_PATH = os.path.dirname(os.path.abspath(__file__))

with open(PRINTR_PATH + '/details.json') as file:
	PRINTR_DETAILS = json_loads(file)


def get_version():
	return PRINTR_DETAILS.version
