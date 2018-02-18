import pandas as pd
from EnergyReadingModel import Reading
import datetime
import testRoutines as stack

# logging.basicConfig(filename='BiggestGreenie.log', level=logging.DEBUG)
# ######################################################################
# get_hour_list(day wanting hourly energy readings)
# This function handles sending back energy readings when the user wants
# to see a plot of energy readings for a specific day.
# Returns 24 average energy readings for the entered day in a list.
# The date format must be MMM D, YYYY.  eg: Jan 21, 2018
# The first element is for the 12AM hour.  The last is for 11PM.
# ######################################################################


def get_hour_list(log,day):
    log.debug('get_hour_list')
    '''get_hour_list(readings for this day)
    returns 24 hourly readings for a specific day.
    The date format must be MMM D, YYYY.  eg: Jan 21, 2018
    The first element is for 12AM.  The last is for 11PM.
    A 0 is returned for an hourly reading if there are
    no entries for that hour.
    '''
    # day is a date string formatted
    start_day_str = day + ' 00 00 00'
    try:
        start_day = datetime.datetime.strptime(
            start_day_str, '%b %d, %Y %H %M %S')
    except ValueError:
        # logging.error(stack.log_line_info() + 'The day passed in - {} - was not valid'.format(start_day))
        return -1
    # Not checking if the end of day is valid since the change was only in hour/min/sec
    end_day_str = day + ' 23 59 59'
    end_day = datetime.datetime.strptime(end_day_str, '%b %d, %Y %H %M %S')
    power_values = get_rows('DAY', start_day, end_day)
    log.debug('power values: {}',power_values)
    return power_values
    ## ######################################################################
    # get_week_list(Monday of the week the user wants energy readings)
    # The date format must be MMM D, YYYY and a Monday.  eg: Jan 21, 2018
    # The first element is for Monday.  The last element is for the following
    # Sunday.  Since there are 7 days in a week, the list returned has 7
    # entries.  0 is returned if the week has no energy readings.
    # ######################################################################


def get_week_list(monday_of_week):
    '''get_week_list(Monday of the week the user wants energy readings)
    returns a list of 7 readings.  The first element is the energy reading
    for Monday.  The 7th element is the energy reading for Sunday.
    'monday_of_week' is a string formated as MMM D, YYYY and a Monday.
                            eg: Jan 21, 2018
    0 is returned for an element if there are no energy readings for the day.
    '''
    # Get energy readings for the day passed in - ie: the Monday of the
    # week, and the subsequent 6 days - ie: full week of readings.
    start_week_str = monday_of_week + ' 00 00 00'
    try:
        start_week = datetime.datetime.strptime(
            start_week_str, '%b %d, %Y %H %M %S')
        # check if the date is a MONDAY.  If it is, .weekday is a Monday.
        if (start_week.weekday() != 0):
            # logging.error(stack.log_line_info() +'The day passed in - {} - is not a Monday'.format(start_week))
            return -1
    except ValueError:
        # logging.error(stack.log_line_info() +'The Monday passed in - {} - is not a valid date'.format(start_day))
        return -1
    end_week = start_week + datetime.timedelta(days=7)
    return get_rows('WEEK', start_week, end_week)


def get_month_list(month, year):
    '''get_month_list(Month within the year to get daily energy readings)
    returns a list where the number of elements is equal to or less than
    the number of days in that month.  The first element is the energy reading
    for the 1st day of the month.  The last element is the energy reading for the
    last day of the month.  The month format must be MMM eg: Jan. The year format
    must be YYYY.
    0 is returned for an element if there are no energy readings for that day.
    '''
    try:
        first_day = datetime.date(year=year, month=month, day=1)
    except ValueError:
        # logging.error(stack.log_line_info() +'Could not create a valid date for month {}, year {}'.format(month,year))
        return -1
    # we know the month, year passed in was valid so the last day will be the right format.
    # we just need to figure out what the last day is.
    first_day = datetime.datetime.combine(first_day,
                                          datetime.time(0, 0, 0))
    last_day = last_day_of_month(first_day)
    last_day = datetime.datetime.combine(last_day,
                                         datetime.time(23, 59, 59))
    return get_rows('MONTH', first_day, last_day)
# ######################################################################
# get_rows is a utility routine used by the functions responsible for
# getting a list of energy readings for a date unit (like 24 hours for a
# day, or 7 days if a week, or weeks if a month....)
# date_unit
# the date_unit input lets get_rows know if the caller wants a list of
# hours (day), days (week), weeks (month), months(year)
# start
# the start input lets get_rows know the start date to use when querying
# the energy reading database.
# stop
# stop lets get_rows know the end date.
# This function handles sending back energy readings when the user wants
# to see a plot of energy readings for a specific day.
# Returns 24 average energy readings for the entered day in a list.
# The date format must be MMM D, YYYY.  eg: Jan 21, 2018
# The first element is for the 12AM hour.  The last is for 11PM.
# ######################################################################


def get_rows(date_unit, start, stop):
    rows_as_peewee = Reading.select(
        Reading.time,
        Reading.p1,
        Reading.p2).where(Reading.time.between(
            start,
            stop))
    # convert a peewee Select() query into a pandas dataframe.
    df = pd.DataFrame(list(rows_as_peewee.dicts()))

    # Our homes have two power lines.  The total power used at a
    # given time is the addition of the two.
    df['power'] = df['p1'] + df['p2']
    # We no longer need the individual power columns.
    df.drop('p1', axis=1, inplace=True)
    df.drop('p2', axis=1, inplace=True)
    # Use the power of Pandas to group the readings
    # into the 'buckets' to be plotted. eg: hour, day readings...
    time_groupings = pd.DatetimeIndex(df.time)
    if (date_unit == 'DAY'):
        groupings = time_groupings.hour
        num_in_list = 24
    elif (date_unit == 'WEEK'):
        groupings = time_groupings.day
        num_in_list = 7
    elif (date_unit == 'MONTH'):
        groupings = time_groupings.day
        num_in_list = last_day_of_month(start).day

    else:
        return -1
    grp = df.groupby([groupings])
    dfs_by_date_unit = [group for _, group in grp]
    y = []
    # 24 hours, 24 entries...there is a possibility there will not
    # be data.  For those entries, I insert a 0...
    for i in range(num_in_list):
        try:
            y.append(dfs_by_date_unit[i].power.mean())
        except IndexError:
            y.append(0)
    return y


# Grabbed this routine from:
# https://stackoverflow.com/questions/42950/get-last-day-of-the-month-in-python


def last_day_of_month(any_day):
    next_month = any_day.replace(
        day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)
