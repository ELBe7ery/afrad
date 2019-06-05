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
                 soldier_id,
                 service_time,
                 max_num_svc=None):
        """
        :param name: Soldier name
        :type name: str

        :param soldier_id: Soldier id
        :type soldier_id: int

        :param service_time: associated solder service time
        :type service_time: soldier.soldier_time.SoldierTime

        :param max_num_svc: limit for # services per scheduling interval (by default the sched. interval is 1 month)
        :type max_num_svc: int | None
        """

        self.__name = name
        self.__soldier_id = soldier_id
        self.__service_time = service_time
        self.__num_services = 0
        self.max_num_svc = max_num_svc

    def add_service(self):
        """
        Adds a single service for the solder
        """
        if self.is_free():
            self.__num_services += 1

    def is_available_for_n_days(self, start_date, n_days):
        """
        returns true if soldier is available starting from the "start_date" for "n_days" number
        of days

        :param start_date: the date to start counting from n_days
        :type start_date : datetime | date
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

    @property
    def name(self):
        return self.__name

    @property
    def soldier_id(self):
        return self.__soldier_id

    def is_free(self):
        if self.max_num_svc is None :
            return True
        return self.__num_services < self.max_num_svc

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

    def __hash__(self):
        return hash(self.__soldier_id)
