
import json
import os


def get_x_axis(date_unit):
    '''Assumes the caller has gotten power readings for a
    date unit such as day, week, month.  The caller passes
    in a date_unit and is returned the x-axis labels.
    For example, if the power readings are for a day, the
    x-axis labels are hours of the day.
    '''
    cwd = os.getcwd()
    with open(cwd+'/x_axis.json') as x_axis_file:
        x_axis_labels = json.load(x_axis_file)
        return  x_axis_labels[date_unit]
