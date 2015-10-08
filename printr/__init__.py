import os
from json import load as json_load

PRINTR_PATH = os.path.dirname(os.path.abspath(__file__))

from .ItterPrintr import ItterPrintr
from .EllipsisPrintr import EllipsisPrintr

with open(PRINTR_PATH + '/../details.json') as file:
	PRINTR_DETAILS = json_load(file)


def get_version():
	return PRINTR_DETAILS.version
