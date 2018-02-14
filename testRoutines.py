#
# This is a utility script run to enable testing of plotting energy readings.
# The EnergyDB has readings for a sampling of dates.  This will allow return
# of readings, but they won't be for the date specified, rather what will
# be returned are readings from the dates available.
# This utility script figures out what unique days are in the Energy DB then
# fills a JSON file as input into test runs.
import datetime
import peewee
import pandas as pd
from EnergyReadingModel import Reading
import inspect
import json
import os
import random

filename = '/Users/margaret/Documents/EnergyMonitoring/HappyDayNeighbors/TheBiggestGreenieV1/uniqueDays.json'


def create_unique_days_file():
    import pdb;pdb.set_trace()
    query = Reading.select()
    df = pd.DataFrame(list(query.dicts()))
    uniqueDays = set()

    for d in df['time']:
        uniqueDay = d.strftime('%b %-d, %Y')
        uniqueDays.add(uniqueDay)
    listUniqueDays = list(uniqueDays)
    print(listUniqueDays)
    with open(filename,'w') as uniqueDaysFile:
        json.dump(listUniqueDays,uniqueDaysFile)
##################################


def get_random_date(typeToReturn):
    isUniqueDaysFile = os.path.isfile(filename)
    if (not isUniqueDaysFile):
        create_unique_days_file()
    with open(filename) as uniqueDaysFile:
        lUnique = json.load(uniqueDaysFile)

        if (typeToReturn == 'any'):
            return(random.choice(lUnique))
        elif (typeToReturn == 'Monday'):
            return(getMonday(lUnique))
        elif (typeToReturn == 'MONTH'):
            return (get_random_month_and_year(lUnique))


def getMonday(lUnique):
    while True:
        day_str = random.choice(lUnique)
        day = datetime.datetime.strptime(day_str, '%b %d, %Y')
        if (day.weekday() == 0):
            return day_str


def get_random_month_and_year(lUnique):
    date_str = random.choice(lUnique)
    date = datetime.datetime.strptime(date_str, '%b %d, %Y')
    return date.month,date.year

def log_line_info():
    return str(inspect.stack()[1][1])+':'+str(inspect.stack()[1][3])+':'+str(inspect.stack()[1][2])+'->'
