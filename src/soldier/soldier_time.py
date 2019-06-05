"""
Soldier time is the object determining the "dof3at" thing in our code.
A soldier time is associated with each Soldier object to indicate his availability over a set of time interval.
"""

import datetime


class InvalidStartEndDate(Exception):
    """
    Thrown in case a ServiceTime available days are invalid.
    """
    pass


class SoldierTime(object):
    """
    Soldier available time (dof3a)
    """

    def __init__(self, display_name, service_id):
        """
        :param display_name: the Service time actual known string name; used for printing and
        debugging purposes
        :type display_name: str
        """
        self.__display_name = display_name
        self.__service_id = service_id
        self.__available_dates = list()

    def add_available_period(self, start_date, end_date):
        """
        Adds the period where this service time is available/exist or ready for serving

        :param start_date: The start date where the service is available.
        :type start_date: datetime

        :param end_date: The last date the service is available
        :type end_date: datetime
        """
        if (start_date >= end_date):
            raise InvalidStartEndDate("Invalid start and end dates. Ensure the start date is before the end date")
        self.__available_dates.append((start_date, end_date))

    def is_available(self, date):
        """
        Checks if the service is available at the given date or not

        :param date: date to check if the service is available at or not
        :type date: date

        :return: returns true if the service is available, otherwise returns false
        :rtype: bool
        """
        for period in self.__available_dates:
            if period[0] <= date <= period[1]: return True
        return False

    @property
    def display_name(self):
        return self.__display_name

    @property
    def service_id(self):
        return self.__service_id

    def __hash__(self):
        return hash(self.__service_id)