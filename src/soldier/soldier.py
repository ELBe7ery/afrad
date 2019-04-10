"""
Implements the soldier entity. Soldiers are the scheduled objects; they are
scheduled over a set of services based on their availability. The scheduling algorithm will
ensure fair service allocation for all the soldiers
"""
import datetime


class Soldier(object):
    """
    Soldier Entity
    """

    def __init__(self,
                 name,
                 service_time):
        """
        :param name: Soldier name
        :type name: str

        :param service_time: associated solder service time
        :type service_time: soldier.soldier_time.SoldierTime
        """

        self.__name = name
        self.__service_time = service_time
        self.__num_services = 0


    def add_service(self):
        """
        Adds a single service for the solder
        """
        self.__num_services += 1


    def is_available_for_n_days(self, start_date, n_days):
        """
        returns true if soldier is available starting from the "start_date" for "n_days" number
        of days

        :param start_date: the date to start counting from n_days
        :type start_date : datetime
        :param n_days: number of days starting from n_days
        :return: true if available and false otherwise
        :rtype: bool
        """
        check_date = start_date
        for i in range(n_days):
            if (not self.__service_time.is_available(check_date)) : return False
            check_date += datetime.timedelta(days=1)
        return True

    @property
    def num_services(self):
        return self.__num_services

    # few overloads for the priority queue
    def __lt__(self,other):
        return self.__num_services < other.__num_services

    def __gt__(self, other):
        return self.__num_services > other.__num_services

    def __eq__(self, other):
        return self.__num_services == other.__num_services

    def __ge__(self, other):
        return self.__num_services >= other.__num_services

    def __le__(self, other):
        return self.__num_services <= other.__num_services

    def __ne__(self, other):
        return self.__num_services != other.__num_services
