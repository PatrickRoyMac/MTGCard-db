# import Python's built-in JSON library
import json, sys
# import the psycopg2 database adapter for PostgreSQL
from psycopg2 import connect, Error
#Get necessary functions
from scryfall_get import *

scry_resp()